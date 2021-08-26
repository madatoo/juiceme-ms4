from django.shortcuts import get_object_or_404
from products.models import Product


def products_in_bag(request):
    """ the contents from here will be available for us in whole app"""

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for product_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity*product.price
        product_count += quantity
        bag_items.append({
            'product_id': product_id, 
            'quantity': quantity,
            'product': product,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }

    return(context)
