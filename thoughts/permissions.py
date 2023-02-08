from rest_framework import permissions
from .models import User, Thought
from rest_framework.views import View
from django.shortcuts import get_object_or_404

import ipdb

class IsAuthenticated(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return request.user.is_authenticated



        