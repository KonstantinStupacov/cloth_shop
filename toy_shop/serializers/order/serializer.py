from rest_framework.serializers import ModelSerializer

from toy_shop.models import OrderDetail


class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'
