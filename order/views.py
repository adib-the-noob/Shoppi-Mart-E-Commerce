from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from .models import Cart
from .serializers import CartSerializer
# Create your views here.

class CartViewSet(ModelViewSet,GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer