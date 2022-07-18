from rest_framework import serializers

from communityapp.models import BoardCategory, Board, Comment, BoardLike


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


class BoardLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardLike
        fields = ['user', 'board', 'created_at', 'updated_at']