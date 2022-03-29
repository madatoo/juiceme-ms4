"""
renders checkout page source CI
"""
import os
import json

from django.shortcuts import (
    render, redirect, reverse, get_object_or_404,
    HttpResponse)
from django.views.decorators.http import require_POST
from django.conf import settings
from django.utils import timezone
from django.contrib import messages

import stripe
from bag.contexts import products_in_bag
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from .forms import OrderForm
from .models import Order, OrderLineItem


@require_POST
def cache_checkout_data(request):
    """ handle the cache data """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed. Try one more time later, please.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """"renders checkout page """
    stripe_public_key = os.getenv('STRIPE_PUBLIC_KEY', '')
    stripe_secret_key = os.getenv('STRIPE_SECRET_KEY', '')

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        order_form_fields = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'postcode': request.POST['postcode'],
            'county': request.POST['county'],

        }
        order_form = OrderForm(order_form_fields)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.orginal_bag = json.dumps(bag)
            order.save()
            total = 0
            bag = request.session.get('bag', {})
            for item_id, quantity in bag.items():
                # try:
                product = Product.objects.get(pk=item_id)
                total += quantity * product.price
                if isinstance(quantity, int):
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
            try:
                customer: stripe.Charge.create(
                    amount=int(total * 100),
                    currency=settings.STRIPE_CURRENCY,
                )
            except Product.DoesNotExist:
                messages.error(
                    request, ("We are sorry. One of the product \
                                in your bag wasen't found in our shop. \
                                Please contact with us for assistance. \
                                Thank you for your cooperation. \
                                We are getting better for you.")
                    )
                order.delete()
                return redirect(reverse("bag_page"))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number]))

        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "Your bag is empty:)")
            return redirect(reverse('products'))

        new_bag = products_in_bag(request)
        new_total = new_bag['total']
        stripe_total = round(new_total*100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempt to prefill the form with any info the
        # user maintains in their profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)

                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'town_or_city': profile.default_town_or_city,
                    'postcode': profile.default_postcode,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.\
            Did you forget to set in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_town_or_city': order.town_or_city,
                'default_postcode': order.postcode,
                'default_county': order.county,
                'default_country': order.country,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        A confirmation email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
