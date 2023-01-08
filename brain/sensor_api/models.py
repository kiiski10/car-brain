from django.db import models
from django.urls import reverse
from sensor_api.validators import validate_command_base_string

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
        default="python3 obd.py {args}",
        validators=[validate_command_base_string],
    )

    def __str__(self):
        return self.string


class BaseSensor(models.Model):
    label = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    unit = None  # Override this in subclass
    command_base = models.ForeignKey(
        CommandBaseString, on_delete=models.PROTECT, blank=True, null=True
    )
    command_args = models.CharField(max_length=250, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}; {}".format(self.label, self.get_unit_display())

    def url(self):
        return reverse("sensor-detail", kwargs={"pk": self.pk})

    def value(self):
        return 1023  # TODO: return value from sensor with `self.command_*`


class Sensor(BaseSensor):
    unit = models.CharField(
        choices=TEMPERATURE_UNITS
        + FLOW_UNITS
        + ROTATION_UNITS
        + HUMIDITY_UNITS
        + SPEED_UNITS
        + PRESSURE_UNITS,
        max_length=5,
    )
