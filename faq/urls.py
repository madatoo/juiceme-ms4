"""views for products"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.faq_all_questions, name='faq_all_questions'),
    
]
