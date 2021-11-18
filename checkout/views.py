import os
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404)
from django.conf import settings
from django.contrib import messages

import stripe
from bag.contexts import products_in_bag
from .forms import OrderForm
from .models import Order, OrderLineItem

from products.models import Product


def checkout(request):
    """"source CI video"""
    stripe_public_key = os.getenv('STRIPE_PUBLIC_KEY', '')
    stripe_secret_key = os.getenv('STRIPE_SECRET_KEY', '')

    if request == 'POST':
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
            'country': request.POST['country'],
        }
        order_form = OrderForm(order_form_fields)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, quantity in bag.items():
                try:
                    product = get_object_or_404(Product, pk=item_id)
                    if isinstance(quantity, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "We are sorry one of the product in your bag wasen't found in our shop. \ Please contact with us for assistance. Thank you for your understanding and cooperation. \ We are getting better for you.")
                    )
                    order.delete()
                    return redirect(reverse("bag_page"))
            
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.id]))

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


def checkout_success(request, pk):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, pk=id)
    messages.success(request, f'Order successfully processed! \
        A confirmation email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
