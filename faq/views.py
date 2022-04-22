"""views for FAQ app"""
from django.shortcuts import (
    render, get_object_or_404)
from .models import FaqPosts


def faq_all_questions(request):
    """ this is the view for all questions"""

    faqs = FaqPosts.objects.all()

    context = {
        'faqs': faqs,
    }

    return render(request, 'faq/faq_questions.html', context)


def single_question(request, faq_id):
    """" view to display single question """
    faq = get_object_or_404(FaqPosts, pk=faq_id)

    context = {
        'faq': faq,
    }

    return render(request, 'faq/single_question.html', context)
