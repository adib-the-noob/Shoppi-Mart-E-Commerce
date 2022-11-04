from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
]
