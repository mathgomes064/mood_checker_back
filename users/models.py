from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    is_manager = models.BooleanField(null=True, default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
