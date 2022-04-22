"""views for FAQ app"""
from django.shortcuts import render
from .models import FaqPosts


def faq_all_questions(request):
    """ this is the view for all questions"""

    faqs = FaqPosts.objects.all()

    context = {
        'faqs': faqs,
    }

    return render(request, 'faq/faq_guestions.html', context)
