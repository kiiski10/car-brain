# Generated by Django 4.1.5 on 2023-01-07 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensor_api', '0002_flowsensor'),
    ]

    operations = [
        migrations.CreateModel(
            name='HumiditySensor',
            fields=[
                ('basesensor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sensor_api.basesensor')),
                ('unit', models.CharField(choices=[('rel', '%'), ('abs', 'g/kg')], max_length=5)),
            ],
            bases=('sensor_api.basesensor',),
        ),
        migrations.CreateModel(
            name='PressureSensor',
            fields=[
                ('basesensor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sensor_api.basesensor')),
                ('unit', models.CharField(choices=[('bar', 'bar'), ('psi', 'psi'), ('kpa', 'kPa')], max_length=5)),
            ],
            bases=('sensor_api.basesensor',),
        ),
        migrations.CreateModel(
            name='RotationSensor',
            fields=[
                ('basesensor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sensor_api.basesensor')),
                ('unit', models.CharField(choices=[('rpm', 'r/m'), ('dpm', 'deg/m')], max_length=5)),
            ],
            bases=('sensor_api.basesensor',),
        ),
        migrations.CreateModel(
            name='SpeedSensor',
            fields=[
                ('basesensor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='sensor_api.basesensor')),
                ('unit', models.CharField(choices=[('kph', 'km/h'), ('mph', 'mi/h')], max_length=5)),
            ],
            bases=('sensor_api.basesensor',),
        ),
        migrations.AddField(
            model_name='basesensor',
            name='command',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='basesensor',
            name='label',
            field=models.CharField(default='sensor', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basesensor',
            name='description',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
