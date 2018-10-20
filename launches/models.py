from django.db import models
from django_countries.fields import CountryField

from ports.models import Port


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
    port = models.ForeignKey(
        Port,
        on_delete=models.CASCADE,
    )

    country = CountryField()

    when = models.DateTimeField()

    payload = models.CharField(
        max_length=100,
    )

    destination = models.CharField(
        max_length=100,
    )
