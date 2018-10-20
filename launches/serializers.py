from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from .models import Launch


class LaunchSerializer(CountryFieldMixin, serializers.ModelSerializer):

    class Meta:

        model = Launch
        fields = '__all__'
