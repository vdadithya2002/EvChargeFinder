from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    preferred_charging_speed = models.CharField(max_length=50, null=True, blank=True)
