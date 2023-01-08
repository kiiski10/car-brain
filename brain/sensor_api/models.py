from django.db import models

TEMPERATURE_UNITS = [
    ("c", "°C"),
    ("k", "K"),
]

FLOW_UNITS = [
    ("lpm", "l/min"),
    ("lph", "l/h"),
]

ROTATION_UNITS = [
    ("rpm", "r/m"),
    ("dpm", "deg/m"),
]

HUMIDITY_UNITS = [
    ("rel", "%"),
    ("abs", "g/kg"),
]

SPEED_UNITS = [
    ("kph", "km/h"),
    ("mph", "mi/h"),
]

PRESSURE_UNITS = [
    ("bar", "bar"),
    ("psi", "psi"),
    ("kpa", "kPa"),
]


class CommandBaseString(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    string = models.CharField(
        max_length=200,
        default="python3 obd.py {args}"
    )

    def __str__(self):
        return self.string


class BaseSensor(models.Model):
    label = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    unit = None       # Override this in subclass
    command_base = models.ForeignKey(CommandBaseString, on_delete=models.PROTECT, null=True)
    command_args = models.CharField(max_length=250, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label

    def read(self):
        return 1023 # TODO: return value from sensor with `self.command_*`


class TempSensor(BaseSensor):
    unit = models.CharField(
        choices=TEMPERATURE_UNITS,
        max_length=5,
    )


class FlowSensor(BaseSensor):
    unit = models.CharField(
        choices=FLOW_UNITS,
        max_length=5,
    )


class RotationSensor(BaseSensor):
    unit = models.CharField(
        choices=ROTATION_UNITS,
        max_length=5,
    )


class SpeedSensor(BaseSensor):
    unit = models.CharField(
        choices=SPEED_UNITS,
        max_length=5,
    )


class HumiditySensor(BaseSensor):
    unit = models.CharField(
        choices=HUMIDITY_UNITS,
        max_length=5,
    )


class PressureSensor(BaseSensor):
    unit = models.CharField(
        choices=PRESSURE_UNITS,
        max_length=5,
    )
