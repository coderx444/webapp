# Generated by Django 3.2.4 on 2021-07-01 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meter', '0004_alter_carddetail_civ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carddetail',
            name='civ',
            field=models.CharField(max_length=3, verbose_name='CVV'),
        ),
    ]
