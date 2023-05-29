from django.urls import path
from .views import ProductViewSet

urlpatterns = [
    path('product/', ProductViewSet.as_view({'get': 'list'}), name='product'),
    path('product/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'}), name='product-detail'),

]