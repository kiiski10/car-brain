from rest_framework import viewsets
from rest_framework import permissions
from sensor_api.models import (
    TempSensor, FlowSensor, RotationSensor,
    SpeedSensor, HumiditySensor, PressureSensor
)
from sensor_api.serializers import (
    TempSensorSerializer, FlowSensorSerializer, RotationSensorSerializer,
    SpeedSensorSerializer, HumiditySensorSerializer, PressureSensorSerializer,
)

class TempSensorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for TempSensor
    """
    queryset = TempSensor.objects.all().order_by('-created')
    serializer_class = TempSensorSerializer
    permission_classes = [permissions.IsAuthenticated]


class FlowSensorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for FlowSensor
    """
    queryset = FlowSensor.objects.all().order_by('-created')
    serializer_class = FlowSensorSerializer
    permission_classes = [permissions.IsAuthenticated]


class RotationSensorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for RotationSensor
    """
    queryset = RotationSensor.objects.all().order_by('-created')
    serializer_class = RotationSensorSerializer
    permission_classes = [permissions.IsAuthenticated]


class SpeedSensorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for SpeedSensor
    """
    queryset = SpeedSensor.objects.all().order_by('-created')
    serializer_class = SpeedSensorSerializer
    permission_classes = [permissions.IsAuthenticated]


class HumiditySensorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for HumiditySensor
    """
    queryset = HumiditySensor.objects.all().order_by('-created')
    serializer_class = HumiditySensorSerializer
    permission_classes = [permissions.IsAuthenticated]


class PressureSensorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for PressureSensor
    """
    queryset = PressureSensor.objects.all().order_by('-created')
    serializer_class = PressureSensorSerializer
    permission_classes = [permissions.IsAuthenticated]