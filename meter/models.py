from django.db import models
from django.contrib.auth import  get_user_model
from authy.models import Profile


class MeterData(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL, null=True)
    usage_of_unit = models.IntegerField()
    meter_reading= models.IntegerField()
    unit_usage_date = models.DateField()

    def __str__(self):
        return str(self.id)


class Bill(models.Model):
    meter_id = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    total_bill = models.IntegerField()
    date = models.DateField(auto_now_add=True)


