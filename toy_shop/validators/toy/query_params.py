from rest_framework.exceptions import ValidationError


class ToyQueryParamValidator:
    def __call__(self, value):
        search_instance = self.model.objects.filter(pk=value).exists()
        if not search_instance:
            raise ValidationError(f"{self.model.__doc__} с id {value} не найден")

    def __init__(self, our_model):
        self.model = our_model

    # Пользователи авторизация заказы
