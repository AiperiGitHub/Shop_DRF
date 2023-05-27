from django.urls import path

from .views import view_cart, add_to_cart, remove_from_cart, place_order, save_order_info, order_confirmation

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('place_order/', place_order, name='place_order'),
    path('save_order_info/', save_order_info, name='save_order_info'),
    path('order_confirmation/', order_confirmation, name='order_confirmation'),
]
