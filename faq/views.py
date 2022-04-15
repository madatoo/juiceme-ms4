"""views for FAQ app"""
from django.shortcuts import (render, redirect,
                              reverse, get_object_or_404)
from .models import FaqPosts


def faq_all_questions(request):
    """ this is the view for all questions"""

    faqpost = FaqPosts.objects.all().order_by('-date_added')

    context = {
        'faqpost': faqpost
    }

    return render(request, 'faq/faq_guestions.html')


def single_question(request, faq_id):
    """ view to display single faq question"""
    faq = get_object_or_404(FaqPosts, pk=faq_id)

    return redirect(reverse('faq/single_guestions.html', args=[faq_id]))
