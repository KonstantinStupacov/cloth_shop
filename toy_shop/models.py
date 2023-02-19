from django.db.models import AutoField, CharField, FloatField, ForeignKey, CASCADE, Model


class Toy(Model):
    uuid = AutoField(primary_key=True)
    name = CharField(max_length=255, verbose_name='Название')
    quantity = FloatField(max_length=20, verbose_name="Количество на складе")
    price = FloatField(max_length=30, verbose_name="Цена")
    uuid_sex = ForeignKey('Sex', on_delete=CASCADE, blank=False, null=False, verbose_name="Пол")
    uuid_category = ForeignKey('Category', on_delete=CASCADE,
                               blank=False, null=False, verbose_name="Категории товара")
    __doc__ = 'Игрушки'

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'№{self.uuid}: {self.name}, в наличии {self.quantity}, цена:{self.price}'


class Sex(Model):
    uuid = AutoField(primary_key=True)
    name = CharField(max_length=255)
    __doc__ = 'Пол'

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'№{self.uuid}: {self.name}'


class Category(Model):
    uuid = AutoField(primary_key=True)
    name = CharField(max_length=255)
    __doc__ = 'Раздел'

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'№{self.uuid}: {self.name}'
