from rest_framework import serializers

from communityapp.models import BoardCategory, Board, Comment


class BoardCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardCategory
        fields = ['kind', 'description']


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['category', 'user', 'title', 'content', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'board', 'content', 'created_at', 'updated_at']