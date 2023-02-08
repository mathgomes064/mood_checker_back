from django.db import models
import uuid


class Mood(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mood = models.IntegerField(blank=True, null=True)
    rate_one = models.IntegerField(blank=True, null=True)
    question_one = models.CharField(max_length=300)
    rate_two = models.IntegerField(blank=True, null=True)
    question_two = models.CharField(max_length=300)
    rate_tree = models.IntegerField(blank=True, null=True)
    question_tree = models.CharField(max_length=300)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="moods"
    )
    created_at = models.DateField(auto_now_add=True)

    REQUIRED_FIELDS = ["mood", "rate_one", "rate_two", "rate_tree"]
