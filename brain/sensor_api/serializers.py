from rest_framework import serializers

from .models import (
    TempSensor, FlowSensor, RotationSensor,
    SpeedSensor, HumiditySensor, PressureSensor,
)


class TempSensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TempSensor
        fields = ['command_args', 'description', 'unit', 'label']


class FlowSensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FlowSensor
        fields = ['command_args', 'description', 'unit', 'label']


class RotationSensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RotationSensor
        fields = ['command_args', 'description', 'unit', 'label']


class SpeedSensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SpeedSensor
        fields = ['command_args', 'description', 'unit', 'label']


class HumiditySensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HumiditySensor
        fields = ['command_args', 'description', 'unit', 'label']


class PressureSensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PressureSensor
        fields = ['command_args', 'description', 'unit', 'label']

