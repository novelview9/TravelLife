from django.db import models


class ChargingStation(models.Model):

    name = models.CharField(
        max_length=20,
    )
    charger_quantity = models.CharField(
        max_length=5,
    )
    charger_type = models.CharField(
        max_length=10,
    )
    address = models.CharField(
        max_length=50,
    )
    latitude = models.FloatField()
    longitude = models.FloatField()
