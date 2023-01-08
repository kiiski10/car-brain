from django.contrib import admin

from sensor_api.models import (
    Sensor,
    CommandBaseString,
)

sensor_api_models = [
    Sensor,
    CommandBaseString,
]

admin.site.register(sensor_api_models)
