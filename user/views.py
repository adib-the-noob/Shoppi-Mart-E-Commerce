from rest_framework import viewsets
from .serializers import UserProfileSerializer, UserRegisterSerializer, UserLoginSerializer
from .models import MyUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated  
from auth.token import get_jwt

# Create your views here.


class UserProfileView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        if serializer.is_valid:
            return Response(serializer.data, status=status.HTTP_200_OK)


class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_jwt(user)
            return Response({'token': token,
                            'data': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                return Response(
                    {
                    'message': 'Login Successful',
                    'token': get_jwt(user),
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response({'error': {'non_field_errors': ['Email or Password is not Valid!']}}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'Login'})
