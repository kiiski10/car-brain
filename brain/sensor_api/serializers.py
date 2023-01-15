from rest_framework import serializers

from .models import OneWireSensor, OBDSensor


class OneWireSensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OneWireSensor
        fields = [
            "pk",
            "command_args",
            "label",
            "value",
            "unit",
            "description",
            "url",
        ]


class OBDSensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OBDSensor
        fields = [
            "pk",
            "command_args",
            "label",
            "value",
            "unit",
            "description",
            "url",
        ]
