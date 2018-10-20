import json

from accounts.models import User
from rest_framework import permissions


class IsPortOrg(permissions.BasePermission):
    """Custom permission to know if user is a port owner
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        user = User.objects.get(username=request.user.username)

        return user.is_portorg
