from django.conf import settings
from products.models import Product


def products_in_bag(request):
    """ the contents from here will be available for us in whole app"""

    bag_products = []
    total = 0
    product_count = 0

    context = {
        'bag_products': bag_products,
        'total': total,
        'product_count': product_count,
    }

    return(context)
