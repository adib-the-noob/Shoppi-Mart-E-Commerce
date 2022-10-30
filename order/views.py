from .models import Cart, CartItem

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

from .serializers import CartSerializer,CartItemSerializer,AddCartItemSerializer
# Create your views here.

class CartViewSet(GenericViewSet,
                ListModelMixin,
                RetrieveModelMixin,
                CreateModelMixin,
                UpdateModelMixin,
                DestroyModelMixin
                    ):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        return CartItemSerializer

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}
    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])
