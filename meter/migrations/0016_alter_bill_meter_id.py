# Generated by Django 3.2.6 on 2022-05-28 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meter', '0015_auto_20220528_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='meter_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
