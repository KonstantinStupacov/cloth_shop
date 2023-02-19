from rest_framework.serializers import ModelSerializer

from ...models import Toy


class ToyModelSerializer(ModelSerializer):
    class Meta:
        model = Toy
        fields = '__all__'

