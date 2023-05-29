from rest_framework import serializers
from .models import Product, Specification, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = '__all__'


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(read_only=True, many=True)  # Используем созданный сериализатор для поля изображения

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'images')


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(read_only=True, many=True)  # Используем созданный сериализатор для поля изображения
    specifications = SpecificationSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = '__all__'




