from rest_framework import serializers

from productapp.models import ProductCategory, Product, Routine


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["name", "description", "kind"]

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["user", "name", "description", "difficulty", "category"]


class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = ["user", "name", "description", "difficulty", "product"]
