from django.db import models

from django_countries.fields import CountryField


class Port(models.Model):

    name = models.CharField(
        max_length=200
    )

    location = models.CharField(
        max_length=200
    )
    country = CountryField()
    lat = models.DecimalField(
        max_digits=13,
        decimal_places=10
    )
    lng = models.DecimalField(
        max_digits=13,
        decimal_places=10,
    )

    website = models.CharField(
        blank=True,
        max_length=100,
    )

    viewpoints = models.CharField(
        blank=True,
        max_length=100,
    )
