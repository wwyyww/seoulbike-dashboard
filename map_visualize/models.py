from django.db import models
from bike_data.models import Station
from bike_data.models import Usage
# Create your models here.
class List_station(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    
class List_usage(models.Model):
    usage = models.ForeignKey(Usage, on_delete=models.CASCADE)