from rest_framework import viewsets, permissions
from django.shortcuts import render
from .serializers import ProductListSerializer, ProductDetailSerializer
from .models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    serializer_classes = {
        'retrieve': ProductDetailSerializer,
    }
    permission_classes = [permissions.IsAuthenticated, ]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)


class RunParserSet(viewsets.ViewSet):
    def retrieve(self, request, date=None):
        # Код для обработки запроса и запуска парсера
        return render(request, 'shops/run_parser.html')
