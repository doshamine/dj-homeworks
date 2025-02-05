from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer

class ListCreateSensors(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class RetrieveUpdateSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class CreateMeasurement(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer