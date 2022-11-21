from .models import Category, Product
from .serializers import CategorySerializer,ProductSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet,GenericViewSet

# Create your views here.



class CategoryViewSet(ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    queryset = Product.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]   
    ordering_fields = ['title', 'price']
    search_fields = ['^title', '=title','^description','=description']
    serializer_class = ProductSerializer


class SingleProductView(APIView):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def patch(self, request, id):
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product, data=request.data,partial=True)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, id):
        product = Product.objects.get(id=id)
        product.delete()
        return Response(status=204)
    

    