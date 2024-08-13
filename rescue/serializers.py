from rest_framework import serializers
from .models import *


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields =('id','model','name')


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'
        