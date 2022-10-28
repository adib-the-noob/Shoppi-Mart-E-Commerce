from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cart', views.CartViewSet)

urlpatterns = router.urls