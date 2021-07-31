from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """"source CI video"""
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty:)")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }

    return render(request, template, context)
