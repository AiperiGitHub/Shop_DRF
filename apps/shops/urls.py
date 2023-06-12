from django.urls import path
from .views import ProductViewSet

urlpatterns = [
    path('product/', ProductViewSet.as_view({'get': 'list'}), name='product'),
    path('product/create/', ProductViewSet.as_view({'post': 'create'}), name='product'),
    path('product/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='product-detail'),

]