from rest_framework.routers import SimpleRouter
from .views import ToyViewSet, OrderViewSet

router = SimpleRouter()
router.register(r'toy', ToyViewSet, basename='Toy')
router.register(r'order', OrderViewSet, basename='Order')

urlpatterns = router.urls
