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
        'stripe_public_key':'pk_test_51JBQNpL9Jkbmn56EGPuQ2CN8xWEMrHBRSKc9Hb9Wf8WE4b28DnBki2IRQAeQJrtdwT062MG0XUJXz97ePGNiPUVj004lq5pk0x',
        'client_secret':'test client secret',
    }

    return render(request, template, context)
