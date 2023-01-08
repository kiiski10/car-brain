from rest_framework import viewsets
from rest_framework import permissions
from sensor_api.models import Sensor
from sensor_api.serializers import SensorSerializer


class SensorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Sensors
    """

    queryset = Sensor.objects.all().order_by("-created")
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticated]
