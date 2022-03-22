"""This file is created for display the user's profile and order history"""
from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def display_profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/display_profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
