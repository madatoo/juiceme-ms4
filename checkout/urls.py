from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<int:pk>', views.checkout_success, name='checkout_success'),
]
