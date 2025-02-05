from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from measurement.models import Sensor, Measurement

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'sensor', 'photo']


class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
