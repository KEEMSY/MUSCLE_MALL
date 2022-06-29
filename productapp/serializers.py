from rest_framework import serializers

from productapp.models import ProductCategory, Product, Routine, Challenge, ProductDetailCategory


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["description", "kind"]

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class ProductDetailCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetailCategory
        fields = ["name", "description", "category"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["user", "name", "description", "difficulty", "category"]


class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = ["user", "product", "quantity"]


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ["user", "routine", "status"]
