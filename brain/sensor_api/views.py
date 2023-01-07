from rest_framework import viewsets
from rest_framework import permissions
from sensor_api.models import TempSensor
from sensor_api.serializers import SensorSerializer


class SensorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for sensors
    """
    queryset = TempSensor.objects.all().order_by('-pin_number')
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticated]
