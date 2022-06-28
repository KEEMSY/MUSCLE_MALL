from rest_framework import serializers

from userapp.models import User, Coach


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ["user", "nickname", "phone_number", "kind",]

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    product_by_user = serializers.SerializerMethodField()

    def get_product_by_user(self, obj):
        category_list = []
        for category in obj.product_set.all():
            category_list.append(category.name)
        return category_list

    interesting_category = serializers.SerializerMethodField()

    def get_interesting_category(self, obj):
        category_list = []
        for product in obj.product_set.all():
            for category in product.category.all():
                category_list.append((category.name, category.kind))
        return category_list

    coach = CoachSerializer(required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password", "fullname", "gender", "coach", "product_by_user", "interesting_category"]

        extra_kwargs = {
            "password": {'write_only': True},

        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
