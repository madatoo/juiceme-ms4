from django.shortcuts import render
from .models import Product


def all_products(request):
    """" view to display all product """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/all_products.html', context)
