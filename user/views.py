from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserProfileSerializer
from .models import MyUser

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserProfileSerializer