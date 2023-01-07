from rest_framework import serializers

from .models import (
    TempSensor, FlowSensor, RotationSensor,
    SpeedSensor, HumiditySensor, PressureSensor,
)


class TempSensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TempSensor
        fields = ['pin_number', 'description', 'unit', 'label', 'command']


class FlowSensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FlowSensor
        fields = ['pin_number', 'description', 'unit', 'label', 'command']


class RotationSensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RotationSensor
        fields = ['pin_number', 'description', 'unit', 'label', 'command']


class SpeedSensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SpeedSensor
        fields = ['pin_number', 'description', 'unit', 'label', 'command']


class HumiditySensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HumiditySensor
        fields = ['pin_number', 'description', 'unit', 'label', 'command']


class PressureSensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PressureSensor
        fields = ['pin_number', 'description', 'unit', 'label', 'command']

