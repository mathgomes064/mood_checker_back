from rest_framework import permissions
from .models import Mood
from rest_framework.views import View


class IsManager(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return request.user.is_authenticated and request.user.is_manager
