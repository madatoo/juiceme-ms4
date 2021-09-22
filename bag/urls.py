from django.urls import path
from .views import bag_page, add_to_bag, update_bag, delete_from_bag


urlpatterns = [
    path('', bag_page, name='bag_page'),
    path('add/<item_id>/', add_to_bag, name='add_to_bag'),
    path('update_bag/<item_id>/', update_bag, name='update_bag'),
    path('delete/<item_id>/', delete_from_bag, name='delete_fom_bag'),
]
