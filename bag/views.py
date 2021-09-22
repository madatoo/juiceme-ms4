from django.shortcuts import render, redirect, reverse, HttpResponse


def bag_page(request):
    """A view to display the bag context page """

    return render(request, 'bag/bag_page.html')


def add_to_bag(request, item_id):
    """ add a quantity for single product to the bag"""
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity

    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """update bag to specified quantity of single product"""
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    print(quantity)
    return redirect(reverse('bag_page'))


def delete_from_bag(request, item_id):
    """
    remove item from bag
    """
    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
