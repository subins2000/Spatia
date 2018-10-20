from django.shortcuts import render
from rest_framework import generics

from .models import Launch
from .permissions import IsSpaceOrg
from .serializers import LaunchSerializer


class Launches(generics.ListCreateAPIView):
    """Get/Add request
    get:
    Get all launch events
    post:
    Add info about a launch event
    """

    serializer_class = LaunchSerializer
    queryset = Launch.objects.all()


class LaunchView(generics.RetrieveUpdateAPIView):
    """Get info about a launch
    """
    serializer_class = LaunchSerializer

    lookup_url_kwarg = 'id'

    permission_classes = (
        IsSpaceOrg,
    )

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        launch = Launch.objects.filter(id=id)
        return launch
