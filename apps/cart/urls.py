from django.urls import path

from .views import CartView, AddToCartView, RemoveFromCartView, PlaceOrderView

urlpatterns = [
    path('', CartView.as_view(), name='view_cart'),
    path('add/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove/<int:cart_item_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('place_order/', PlaceOrderView.as_view(), name='place_order'),
    # path('save_order_info/', save_order_info, name='save_order_info'),
    # path('order_confirmation/', order_confirmation, name='order_confirmation'),
]

