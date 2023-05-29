from rest_framework import serializers
from .models import Product, Specification


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id',
            'url',
            'product',
            'image',
        )  # Указываем только поле изображения


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = (
            'id',
            'url',
            'name',
            'value',
            'product',
        )


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




