from django.shortcuts import render
from rest_framework import generics, filters

from .models import Port
from .permissions import IsPortOrg
from .serializers import PortSerializer


class Ports(generics.ListCreateAPIView):
    """Get/Add request
    get:
    Get all sapceports
    post:
    Add info about a spaceport
    """

    serializer_class = PortSerializer
    queryset = Port.objects.all()

    filter_backends = (
        filters.OrderingFilter,
    )


class PortView(generics.RetrieveUpdateAPIView):
    """Get info about a launch
    """
    serializer_class = PortSerializer

    lookup_url_kwarg = 'id'

    permission_classes = (
        IsPortOrg,
    )

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        port = Port.objects.filter(id=id)
        return port
