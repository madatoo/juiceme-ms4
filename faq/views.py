"""views for FAQ app"""
from django.shortcuts import render
from .models import FaqPosts


def faq_all_questions(request):
    """ this is the view for all questions"""

    all_questions = FaqPosts.objects.all().order_by('-date_added')

    context = {
        'all_questions': all_questions
    }

    return render(request, 'faq/faq_guestions.html')
