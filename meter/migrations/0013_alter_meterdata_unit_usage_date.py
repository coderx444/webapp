# Generated by Django 3.2.6 on 2022-05-18 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meter', '0012_meterdata_unit_usage_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meterdata',
            name='unit_usage_date',
            field=models.DateField(),
        ),
    ]
