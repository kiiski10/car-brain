from rest_framework import viewsets
from rest_framework import permissions
from sensor_api.models import OBDSensor, OneWireSensor
from sensor_api.serializers import OBDSensorSerializer, OneWireSensorSerializer


class OneWireSensorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for sensors using Dallas 1-Wire protocol
    """

    queryset = OneWireSensor.objects.all().order_by("-created")
    serializer_class = OneWireSensorSerializer
    permission_classes = [permissions.IsAuthenticated]


class OBDSensorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for OBD2 sensors
    """

    queryset = OBDSensor.objects.all().order_by("-created")
    serializer_class = OBDSensorSerializer
    permission_classes = [permissions.IsAuthenticated]
