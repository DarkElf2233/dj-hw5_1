
from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=90, blank=True)


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, related_name='measures', on_delete=models.CASCADE)
    temperature = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
