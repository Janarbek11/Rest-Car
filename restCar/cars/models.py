from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Car(models.Model):
    vin = models.CharField("ВИН", db_index=True, unique=True, max_length=20)
    color = models.CharField('Цвет', max_length=25)
    brand = models.CharField('Бренд', max_length=25)
    CAR_TYPES = (
        (1, 'Седан'),
        (2, "Универсал"),
        (3, 'Хетчбек'),
        (4, 'Внедорожник'),
        (5, 'Спортивный'),
        (6, 'Паркетник'),
    )
    car_type = models.IntegerField('Тип машины', choices=CAR_TYPES, default='Выберите машину')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
