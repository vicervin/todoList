from rest_framework.permissions import BasePermission
from .models import ToDoList

class IsOwner(BasePermission):
    """Custom permission class to allow only todolist owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the todolist owner."""
        if isinstance(obj, ToDoList):
            return obj.owner == request.user
        return obj.owner == request.user