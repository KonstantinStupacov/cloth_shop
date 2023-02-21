from rest_framework.viewsets import ModelViewSet

from toy_shop.models import Order
from toy_shop.serializers.order.serializer import OrderModelSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderModelSerializer

    def get_queryset(self):
        queryset = Order.objects.all()
        return queryset
