from django.shortcuts import render

# Create your views here.

def index (request):
    """A view to return the home page (index.html) """

    return render (request, "home/index.html")
