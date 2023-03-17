from rest_framework.viewsets import ModelViewSet

from ..models import Toy
from ..serializers.toy import ToyModelSerializer, ToyQueryParamsSerializer


class ToyViewSet(ModelViewSet):
    serializer_class = ToyModelSerializer12

    def get_queryset(self):
        queryset = Toy.objects.all()
        if self.action == 'list':
            return self.get_filtered_queryset(queryset)
        return queryset

    def get_filtered_queryset(self, queryset):
        query_params = self.request.query_params
        serializer = ToyQueryParamsSerializer(data=query_params)
        serializer.is_valid(raise_exception=True)
        filter_data = {
            f'uuid_{key}': value
            for key, value in serializer.validated_data.items()
        }
        return queryset.filter(**filter_data)
