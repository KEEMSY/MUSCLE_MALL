from rest_framework import serializers

from communityapp.models import BoardCategory, Board


class BoardCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardCategory
        fields = ['kind', 'description']


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['category', 'title', 'content', 'created_at']
