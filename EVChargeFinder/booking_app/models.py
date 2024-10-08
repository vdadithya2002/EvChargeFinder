from django.db import models
from django.contrib.auth import get_user_model
from charging_stations_app.models import ChargingStation

User = get_user_model()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    charging_station = models.ForeignKey(ChargingStation, on_delete=models.CASCADE)
    date = models.DateField(default='2024-01-01')
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=50, choices=[('Booked', 'Booked'), ('Cancelled', 'Cancelled')])

    def __str__(self):
        return f"{self.user.username} - {self.charging_station.name} - {self.start_time}"

