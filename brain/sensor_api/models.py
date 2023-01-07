from django.db import models


TEMPERATURE_UNITS = [
    ("c", "°C"),
    ("k", "K"),
]


class BaseSensor(models.Model):
    pin_number = models.CharField(max_length=5)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.pin_number


class TempSensor(BaseSensor):
    unit = models.CharField(
        choices=TEMPERATURE_UNITS,
        max_length=5
    )
