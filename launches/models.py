from django.db import models

from django_countries.fields import CountryField


class Launch(models.Model):

    id = models.AutoField(
        primary_key=True,
        help_text='Unique ID of launch event',
    )
    name = models.CharField(
        blank=True,
        max_length=100,
        help_text='Name of launch',
    )
    rocket = models.CharField(
        max_length=100,
        help_text='Name of rocket',
    )

    location = models.CharField(
        max_length=100,
        help_text='Location'
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
