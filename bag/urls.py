from django.urls import path
from .views import bag_page, add_to_bag, update_bag


urlpatterns = [
    path('', bag_page, name='bag_page'),
    path('add/<int:product_id>/', add_to_bag, name='add_to_bag'),
    path('update/<int:product_id>/', update_bag, name='update_bag'),
]
