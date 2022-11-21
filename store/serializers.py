from .models import Category, Product,Review
from rest_framework import serializers
from user.serializers import UserProfileSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    alt = serializers.SerializerMethodField()
    category = CategorySerializer()

    def get_alt(self,product : Product):    
        return product.title

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'price',
            'category',
            'image',
            'alt',
        ]

    def create(self, validated_data):
        category = validated_data.pop('category')
        category = Category.objects.get_or_create(**category)[0]            
        return Product.objects.create(category=category, **validated_data)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user','product','review','date_added']

    def create(self, validated_data):
        product_id = self.context.get('product_id')
        return Review.objects.create(product_id=product_id, **validated_data)       