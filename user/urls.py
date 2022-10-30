from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', views.UserViewSet, basename='user')

urlpatterns = [
    
]

urlpatterns += router.urls