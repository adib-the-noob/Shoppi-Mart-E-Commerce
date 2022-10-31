from .models import Category, Product
from rest_framework import serializers



class ProductSerializer(serializers.ModelSerializer):

    alt = serializers.SerializerMethodField()
    def get_alt(self,product : Product):
        return product.title

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'price',
            'image',
            'alt',
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

