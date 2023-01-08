from django.contrib import admin

from sensor_api.models import (
    TempSensor, FlowSensor, RotationSensor,
    SpeedSensor, HumiditySensor, PressureSensor,
    CommandBaseString,
)

sensor_api_models = [
    TempSensor, FlowSensor, RotationSensor,
    SpeedSensor, HumiditySensor, PressureSensor,
    CommandBaseString,
]

admin.site.register(sensor_api_models)
