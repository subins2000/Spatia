from django.db import models


class Port(models.Model):

    name = models.CharField(
        max_length=200
    )

    location = models.CharField(
        max_length=200
    )
    country = CountryField()
    lat = models.DecimalField(
        max_digits=9,
        decimal_places=6
    )
    lng = models.DecimalField(
        max_digits=9,
        decimal_places=6
    )
