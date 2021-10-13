from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages

from .forms import OrderForm
from .models import Order, OrderLineItem

import os
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    """"source CI video"""
    stripe_public_key = os.getenv('STRIPE_PUBLIC_KEY', '')
    stripe_secret_key = os.getenv('STRIPE_SECRET_KEY', '')

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty:)")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        }

    return render(request, template, context)
