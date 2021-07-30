from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.bag_page, name='bag_page'),
    path('add/<product_id>/', views.add_to_bag, name='add_to_bag'),
]
