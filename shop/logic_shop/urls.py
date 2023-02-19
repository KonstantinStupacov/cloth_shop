from rest_framework.routers import SimpleRouter
from .views import ToyViewSet

router = SimpleRouter()
router.register(r'toy', ToyViewSet, basename='Toy')

urlpatterns = router.urls
