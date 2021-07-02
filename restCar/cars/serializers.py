from rest_framework import serializers
from .models import *


class CarListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'vin', 'brand', 'user')


class CarDetailSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = "__all__"

# class CarDetailSerializers(serializers.ModelSerializer):