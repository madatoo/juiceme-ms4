from django.shortcuts import render, redirect

# Create your views here.

def bag_page(request):
    """A view to display the bag context page """

    return render(request, "bag/bag_page.html")


def add_to_bag(request, product_id):
    """ add  a quantity product to the bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity
   
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
