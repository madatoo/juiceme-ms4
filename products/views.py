from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """" view to display all product """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/all_products.html', context)


def single_product(request, product_id):
    """" view to display single product """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/single_product.html', context)
