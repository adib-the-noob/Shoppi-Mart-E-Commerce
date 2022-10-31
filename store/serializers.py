from .models import Category, Product
from rest_framework import serializers



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'price',
            'image',
        ]


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug',
            'products',
        ]

