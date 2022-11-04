from .models import Category, Product
from .serializers import CategorySerializer,ProductSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.



class CategoryViewSet(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(ListAPIView):
    queryset = Product.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]   
    search_fields = ['title', 'description',]
    serializer_class = ProductSerializer


class ProductDetails(APIView):
    def get(self, request, title):
        product = Product.objects.filter(title__icontains=title)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
