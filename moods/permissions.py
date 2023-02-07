from rest_framework import permissions
from .models import Mood
from rest_framework.views import View


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Mood) -> bool:
        return request.user.is_authenticated
