from rest_framework import serializers

from userapp.models import User, Coach


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ["user", "nickname", "phone_number", "kind", "approved_coach"]
        extra_kwargs = {
            "approved_coach": {'write_only': True},

        }

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    coach = CoachSerializer(required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password", "fullname", "gender", "coach", "bind_number", "approved_user"]

        extra_kwargs = {
            "password": {'write_only': True},

        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
                continue
            elif key == "bind_number":
                value += 1

            setattr(instance, key, value)
        instance.save()
        return instance

