# Generated by Django 3.2.6 on 2022-05-15 22:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meter', '0010_auto_20210704_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeterData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usage_of_unit', models.IntegerField()),
                ('power_status', models.BooleanField(default=False)),
                ('meter_reading', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_bill', models.FloatField()),
                ('date', models.DateField()),
                ('meter_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meter.meterdata')),
            ],
        ),
    ]