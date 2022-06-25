from rest_framework import serializers

from userapp.models import User, Coach


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ["user", "nickname", "phone_number", "kind"]

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    coach = CoachSerializer(required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password", "fullname", "gender", "coach"]

        extra_kwargs = {
            "password": {'write_only': True},

        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
