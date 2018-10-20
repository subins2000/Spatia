from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from .models import Port


class PortSerializer(CountryFieldMixin, serializers.ModelSerializer):

    class Meta:

        model = Port
        fields = '__all__'
