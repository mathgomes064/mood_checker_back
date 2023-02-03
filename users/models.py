from django.db import models
import uuid


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField()
    isManager = models.BooleanField(null=True, default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
