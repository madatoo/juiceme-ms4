from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_products(request):

    """" view to display all product """
    products = Product.objects.all()
    search = None
    categories = None

    if request.GET:

        """" sorting by category"""
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        """here we can serch by serch criteria in products 
        and in product descriptions"""
        if 'q' in request.GET:
            """ serch by entered criteria """ 
            search = request.GET['q']
            """ messege about not entered search criteria"""
        if not search:
            messages.error(request, "Please enter the search criteria.")
            return redirect(reverse('products'))

        queries = Q(name__icontains=search) | Q(
            description__icontains=search) 
        products = products.filter(queries)

    context = {
        'products': products,
        'search_term': search,
        'current_categories': categories,
    }

    return render(request, 'products/all_products.html', context)


def single_product(request, product_id):
    """" view to display single product """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/single_product.html', context)
