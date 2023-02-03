from rest_framework import serializers
from .models import Thought


class ThoughtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thought
        fields = [
            "id",
            "thought",
            "user",
            "created_at",
        ]
