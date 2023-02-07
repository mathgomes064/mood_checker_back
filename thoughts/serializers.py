from rest_framework import serializers
from .models import Thought


class ThoughtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thought
        fields = [
            "id",
            "thought",
            "user_id",
        ]
        read_only_fields = ["id", "user_id"]

    def create(self, validated_data):
        return Thought.objects.create(**validated_data)
