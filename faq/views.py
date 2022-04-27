"""views for FAQ app"""
from django.shortcuts import (
    render, get_object_or_404, redirect, reverse)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import FaqPosts
from .forms import FaqPostsForm


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


@login_required()
def add_question(request):
    """ Add a question to the FAQ list"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can add \
            the question to the FAQ list.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FaqPostsForm(request.POST, request.FILES)
        if form.is_valid():
            faq = form.save()
            messages.success(request, "FAQ post successfuly added.")
            return redirect(reverse('single_question', args=[faq.id]))
        else:
            messages.error(
                request, "Something went wrong. \
                Please enter the all details again and \
                make sure they are correct.")
    else:
        form = FaqPostsForm()

    template = 'faq/add_question.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required()
def edit_question(request, faq_id):
    """ view for editing FAQ post by the admin"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can add \
            the question to the FAQ list.')
        return redirect(reverse('home'))

    faq = get_object_or_404(FaqPosts, pk=faq_id)
    if request.method == 'POST':
        form = FaqPostsForm(request.POST, request.FILES, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, "FAQ Post successfuly edited.")
            return redirect(reverse('single_question', args=[faq.id]))
        else:
            messages.error(request, "Something went wrong. \
                Please enter the details again.")
    else:
        form = FaqPostsForm(instance=faq)
        messages.info(request, f'You are editing {faq.question}')

    template = 'faq/edit_question.html'
    context = {
        'form': form,
        'faq': faq
    }

    return render(request, template, context)


@login_required()
def delete_question(request, faq_id):
    """ Delete product from store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    faq = get_object_or_404(FaqPosts, pk=faq_id)
    faq.delete()
    messages.success(request, 'FAQ post deleted!')
    return redirect(reverse('faq_all_questions'))

