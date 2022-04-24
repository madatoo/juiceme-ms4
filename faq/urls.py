"""views for products"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.faq_all_questions, name='faq_all_questions'),
    path('<int:faq_id>/', views.single_question, name='single_question'),
    path('add/', views.add_question, name='add_question'),
    path('edit/<int:faq_id>/', views.edit_question, name='edit_question'),
    path('delete/<int:faq_id>/', views.delete_question,
         name='delete_question'),
]
