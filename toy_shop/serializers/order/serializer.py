from rest_framework.serializers import ModelSerializer

from toy_shop.models import OrderDetail, Order
from toy_shop.serializers.toy import ToyModelSerializer


class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'


class OrderMSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    toy = ToyModelSerializer(read_only=True)
