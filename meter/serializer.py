from rest_framework import serializers
from .models import MeterData
from authy.models import Profile


class MeterDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeterData
        fields = ['usage_of_unit', 'meter_reading', 'unit_usage_date', 'user']


class MeterDataListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'power_status']