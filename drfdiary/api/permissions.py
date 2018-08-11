from rest_framework import permissions
from .models import Entry


class IsOwner(permissions.BasePermission):
    """
    Custom permission class to allow only bucketlist owners to edit them.
    """


    def has_object_permission(self, request, view, obj):
        """
        Return True id permission is granted to the bucketlist owner
        """
        if isinstance(obj, Entry):
            return obj.owner == request.user
        return obj.owner == request.user
