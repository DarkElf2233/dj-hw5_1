
from django.urls import path
from .views import SensorsView, SensorDetailView, MeasureView

app_name = 'measurement'

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensor-detail/<int:sensor_id>/', SensorDetailView.as_view()),
    path('measure/', MeasureView.as_view())
]
