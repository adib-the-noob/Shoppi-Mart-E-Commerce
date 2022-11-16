from django.urls import path
from . import views
 
urlpatterns = [
    path('categories/', views.CategoryViewSet.as_view()),
    path('products/', views.ProductViewSet.as_view()),
    path('product/<int:id>/', views.ProductDetails.as_view()),
]