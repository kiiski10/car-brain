from .models import TempSensor
from rest_framework import serializers


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TempSensor
        fields = ['pin_number', 'description', 'unit']

