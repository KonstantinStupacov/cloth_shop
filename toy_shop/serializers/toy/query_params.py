from rest_framework.fields import IntegerField
from rest_framework.serializers import Serializer

from toy_shop.models import Sex, Category
from toy_shop.validators import ToyQueryParamValidator


class ToyQueryParamsSerializer(Serializer):
    sex = IntegerField(validators=[ToyQueryParamValidator(Sex)], required=False)
    category = IntegerField(validators=[ToyQueryParamValidator(Category)], required=False)
