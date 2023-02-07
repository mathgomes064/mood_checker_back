from rest_framework import serializers
from .models import Mood


class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = [
            "mood",
            "rate_one",
            "question_one",
            "rate_two",
            "question_two",
            "rate_tree",
            "question_tree",
            "user_id",
        ]
        read_only_fields = ["id", "user_id"]

    def create(self, validated_data):
        return Mood.objects.create(**validated_data)
