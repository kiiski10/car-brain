from django.contrib import admin

from sensor_api.models import (
    OneWireSensor,
    OBDSensor,
    CommandBaseString,
)

sensor_api_models = [
    OneWireSensor,
    OBDSensor,
    CommandBaseString,
]

admin.site.register(sensor_api_models)
