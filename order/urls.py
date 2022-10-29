from . import views
from rest_framework import routers
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('cart', views.CartViewSet)

carts_router = routers.NestedDefaultRouter(router, 'cart', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-item-details')

urlpatterns = router.urls + carts_router.urls