"""views for FAQ app"""
from django.shortcuts import (render, redirect,
                              reverse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

    # opinions = CommentsFaqPost.objects.filter(comment=faq)

    return redirect(reverse('faq/single_guestion.html', args=[faq_id]))


@login_required()
def add_question(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FaqPostsForm(request.POST, request.FILES)
        if form.is_valid():
            faq = form.save()
            messages.success(request, "Question successfuly added.")
            return redirect(reverse('single_question', args=[faq.id]))
        else:
            messages.error(
                request, "Something went wrong. \
                Please enter the product details again.")
    else:
        form = FaqPostsForm(instance=faq)

    template = 'faq/add_question.html'
    context = {
            'form': form,
        }

    return render(request, template, context)
