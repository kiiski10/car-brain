from django.contrib import admin
from sensor_api.models import (
    TempSensor, FlowSensor, RotationSensor,
    SpeedSensor, HumiditySensor, PressureSensor
)

admin.site.register(TempSensor)
admin.site.register(FlowSensor)
admin.site.register(RotationSensor)
admin.site.register(SpeedSensor)
admin.site.register(HumiditySensor)
admin.site.register(PressureSensor)