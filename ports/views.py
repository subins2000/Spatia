from django.shortcuts import render


class Ports(generics.ListCreateAPIView):
    """Get/Add request
    get:
    Get all sapceports
    post:
    Add info about a spaceport
    """

    serializer_class = LaunchSerializer
    queryset = Launch.objects.all()


class PortView(generics.RetrieveUpdateAPIView):
    """Get info about a launch
    """
    serializer_class = PortSerializer

    lookup_url_kwarg = 'id'

    permission_classes = (
        IsSpaceOrg,
    )

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        launch = Launch.objects.filter(id=id)
        return launch
