from django.shortcuts import render
from rest_framework.viewsets import (
    ModelViewSet,
    GenericViewSet,
)
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)

from .models import Cart
from .serializers import CartSerializer
# Create your views here.

class CartViewSet(  GenericViewSet,
                    ListModelMixin,
                    RetrieveModelMixin,
                    CreateModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin
                    ):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer