from django.urls import path

from measurement.views import CreateMeasurement, ListCreateSensors, RetrieveUpdateSensor

urlpatterns = [
    path('sensors/', ListCreateSensors.as_view()),
    path('sensors/<pk>/', RetrieveUpdateSensor.as_view()),
    path('measurements/', CreateMeasurement.as_view()),
]
