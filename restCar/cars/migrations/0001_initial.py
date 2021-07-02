# Generated by Django 3.2.5 on 2021-07-01 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='ВИН')),
                ('color', models.CharField(max_length=25, verbose_name='Цвет')),
                ('brand', models.CharField(max_length=25, verbose_name='Бренд')),
                ('car_type', models.IntegerField(choices=[(1, 'Седан'), (2, 'Универсал'), (3, 'Хетчбек'), (4, 'Внедорожник'), (5, 'Спортивный'), (6, 'Паркетник')], default='Выберите машину', verbose_name='Тип машины')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
