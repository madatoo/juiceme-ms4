"""contex"""
from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.conf import settings
from products.models import Product
from profiles.models import UserProfile


def products_in_bag(request):
    """ the contents from here will be available for us in whole app"""

    bag = request.session.get('bag', {})
    bag_items = []
    total = 0
    product_count = 0
    delivery = total * Decimal(settings.STANDARD_DELIVERY / 100)

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product
        })

    if request.user.is_authenticated:
        discount = total * Decimal(settings.CUSTOMER_DISCOUNT / 100)
    else:
        discount = total * Decimal(settings.GUEST_DISCOUNT / 100)

    total = total - (discount + delivery)

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'discount': discount,
        'delivery': delivery
    }

    return context
