from django.db import models
import uuid


class MoodRating(models.TextChoices):
    VERY_SAD = "Very sad"
    SAD = "Sad"
    OK = "Ok"
    HAPPY = "Happy"
    VERY_HAPPY = "Very Happy"


class Mood(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mood = models.CharField(
        max_length=20, choices=MoodRating.choices, default=MoodRating.OK
    )
    rate_one = models.IntegerField(blank=True, null=True)
    question_one = models.CharField(max_length=300)
    rate_two = models.IntegerField(blank=True, null=True)
    question_two = models.CharField(max_length=300)
    rate_tree = models.IntegerField(blank=True, null=True)
    question_tree = models.CharField(max_length=300)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="moods"
    )
    # created_at = models.DateField(auto_now=True)

    REQUIRED_FIELDS = ["mood", "rate_one", "rate_two", "rate_tree"]
