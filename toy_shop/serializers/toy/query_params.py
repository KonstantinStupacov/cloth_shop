from rest_framework.fields import IntegerField
from rest_framework.serializers import Serializer

from ...models import Category, Sex
from ...validators.model_exists_query_param import ModelExistsQueryParamValidator


class ToyQueryParamsSerializer(Serializer):
    sex = IntegerField(validators=[ModelExistsQueryParamValidator(Sex)], required=False)
    category = IntegerField(validators=[ModelExistsQueryParamValidator(Category)], required=False)

