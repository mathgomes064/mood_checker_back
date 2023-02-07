from django.db import models
import uuid
from users.models import User


class Thought(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    thought = models.CharField(max_length=300)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="thoughts"
    )
    created_at = models.DateField(auto_now_add=True)
