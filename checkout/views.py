import os
from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages

import stripe
from bag.contexts import products_in_bag
from .forms import OrderForm
from .models import Order, OrderLineItem

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    """"source CI video"""
    stripe_public_key = os.getenv('STRIPE_PUBLIC_KEY', '')
    stripe_secret_key = os.getenv('STRIPE_SECRET_KEY', '')

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

    print(intent)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        }

    return render(request, template, context)
