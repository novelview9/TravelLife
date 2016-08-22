from django.db import models


class TouristSpotData(models.Model):

    title = models.CharField(
        max_length=256,
    )

    group = models.CharField(
        max_length=256,
    )

    address = models.TextField()

    area_code = models.CharField(
        max_length=8,
    )

    latitude = models.CharField(
        max_length=64,
    )

    longitude = models.CharField(
        max_length=64,
    )

    image_url = models.URLField(
        max_length=200,
        blank=True,
        null=True,
    )

    thumbnailimage_url = models.URLField(
        max_length=200,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
