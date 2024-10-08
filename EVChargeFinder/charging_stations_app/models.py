from django.db import models

class ChargingStation(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    total_slots = models.IntegerField()
    available_slots = models.IntegerField()
    charging_slots = models.IntegerField()
    charging_types = models.CharField(max_length=200)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
