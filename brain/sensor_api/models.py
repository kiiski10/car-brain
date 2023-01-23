from django.db import models
from sensor_api.validators import validate_command_base_string
from sensor_api.sensor_types import onewire

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
    ("dpm", "deg/sec"),
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

ONE_WIRE_SERVICE = onewire.OneWireService()

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
    unit = models.CharField(
        choices=TEMPERATURE_UNITS
        + FLOW_UNITS
        + ROTATION_UNITS
        + HUMIDITY_UNITS
        + SPEED_UNITS
        + PRESSURE_UNITS,
        max_length=10,
        blank=True,
        null=True,
    )
    command_base = models.ForeignKey(
        CommandBaseString, on_delete=models.PROTECT, blank=True, null=True
    )
    address = models.CharField(max_length=250, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}; {}".format(self.label, self.get_unit_display())

    def value(self):
        pass # override in subclass


class OneWireSensor(BaseSensor):
    def value(self):
        return ONE_WIRE_SERVICE.sensors[self.address].read()


class OBDSensor(BaseSensor):
    sensor_oid = models.CharField(max_length=30, blank=True)
    
    def value(self):
        # TODO: retrive the value with pyobd library
        return 3.13243645867