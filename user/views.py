from rest_framework import viewsets
from .serializers import UserProfileSerializer,UserRegisterSerializer
from .models import MyUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class UserProfileView(APIView):
    def get(self,request):
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

class UserRegisterView(APIView):
    def post(self,request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

