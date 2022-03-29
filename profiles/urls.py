"""view for user profile"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.display_profile, name='display_profile'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
]
