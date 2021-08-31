from django.shortcuts import get_object_or_404
from products.models import Product


def products_in_bag(request):
    """ the contents from here will be available for us in whole app"""

    bag = request.session.get('bag', {})
    total = 0
    product_count = 0
    bag_items = []
    print(bag)

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({'item_id': item_id,
                          'quantity': quantity,
                          'product': product})

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }
    # print(context)
    # print(f"{bag_items} items")
    for item_id in bag_items:
        print(f"{item_id['id']} item")

    return(context)
