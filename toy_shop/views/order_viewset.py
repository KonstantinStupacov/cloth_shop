from django.db.models import Prefetch, Count, Sum
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.viewsets import ModelViewSet

from toy_shop.models import Order, Toy, OrderDetail
from toy_shop.serializers.order import OrderModelSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderModelSerializer
    queryset = Order.objects.all()

    def retrieve(self, request, pk: int = None, *args, **kwargs):
        instance = OrderDetail.objects.prefetch_related(
            Prefetch('toy', Toy.objects.all())
        ).filter(
            order_uuid=pk
        ).first()

        if instance is None:
            return Response(status=HTTP_404_NOT_FOUND)

        queryset = instance.toy

