# Generated by Django 4.1.5 on 2023-01-15 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sensor_api", "0018_basesensor_unit"),
    ]

    operations = [
        migrations.AddField(
            model_name="obdsensor",
            name="sensor_oid",
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
