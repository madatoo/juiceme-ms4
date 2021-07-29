from django.shortcuts import render

# Create your views here.

def bag_page (request):
    """A view to display the bag context page """

    return render (request, "bag/bag_page.html")