# Generated by Django 4.1.5 on 2023-01-15 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sensor_api", "0016_obdsensor_rename_sensor_onewiresensor"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="onewiresensor",
            name="unit",
        ),
    ]
