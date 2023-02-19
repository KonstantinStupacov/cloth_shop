from rest_framework.fields import IntegerField
from rest_framework.serializers import Serializer

from ...models import Category, Sex
from ...validators.toy_query_params import ToyQueryParamValidator


class ToyQueryParamsSerializer(Serializer):
    sex = IntegerField(validators=[ToyQueryParamValidator(Sex)], required=False)
    category = IntegerField(validators=[ToyQueryParamValidator(Category)], required=False)

