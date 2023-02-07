from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "is_superuser",
        ]
        extra_kwargs = {
            "id": {
                "read_only": True,
            },
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                    )
                ],
                "required": True,
            },
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                    )
                ],
                "required": True,
            },
            "password": {
                "write_only": True,
                "required": True,
            },
            "is_superuser": {
                "read_only": True,
            },
        }
        
    def create(self, validated_data: dict) -> User:
        return User.objects.create_superuser(**validated_data)

    # def create(self, validated_data):
    #     for key, value in validated_data.items():
    #         if key == "is_manager":
    #             if value == True:
    #                 return User.objects.create_superuser(**validated_data)
    #             return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
