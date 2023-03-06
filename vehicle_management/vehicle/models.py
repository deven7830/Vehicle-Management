from django.db import models
from .validators import vehicle_number_validator


VEHICLE_TYPES = [
    ("Two Wheeler", "Two Wheeler"),
    ("Three Wheeler", "Three Wheeler"),
    ("Four Wheeler", "Four Wheeler"),
]

class VehicleModel(models.Model):
    vehicle_number = models.CharField(max_length=20, validators=[vehicle_number_validator], blank=False, null=False, unique=True)
    vehicle_type = models.CharField(
        max_length = 20, 
        choices=VEHICLE_TYPES, 
        )
    vehicle_model = models.CharField(max_length=100)
    vehicle_description = models.TextField()
