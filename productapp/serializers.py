from rest_framework import serializers

from productapp.models import ProductCategory, Product, Routine


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["name", "description", "kind"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description", "difficulty", "category"]


class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = ["user", "name", "description", "difficulty", "product"]
