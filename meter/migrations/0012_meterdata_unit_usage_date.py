# Generated by Django 3.2.6 on 2022-05-18 21:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meter', '0011_bill_meterdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='meterdata',
            name='unit_usage_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
