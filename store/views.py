from .models import Category, Product
from .serializers import CategorySerializer,ProductSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.



class CategoryViewSet(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ProductViewSet(ListAPIView,):
    queryset = Product.objects.all()[0:10]
    serializer_class = ProductSerializer



class ProductDetails(APIView):
    def get(self, request, slug):
        product = Product.objects.get(slug=slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
