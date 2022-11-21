from django.urls import path
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)

from rest_framework_nested import routers

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

urlpatterns = [
    path('categories/', views.CategoryViewSet.as_view()),
    # path('products/', views.ProductViewSet.as_view()),
    # path('product/<int:id>/', views.SingleProductView.as_view()),
]

urlpatterns += router.urls + product_router.urls