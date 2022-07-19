from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from communityapp.models import BoardCategory, Board, Comment, BoardLike, BoardBookmark


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
    def create(self, validated_data):
        try:
            return super().create(validated_data)

        except IntegrityError as error:
            raise ValidationError from error

    class Meta:
        model = BoardLike
        fields = ['user', 'board', 'created_at', 'updated_at']


class BookmarkBoardSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        try:
            return super().create(validated_data)

        except IntegrityError:
            raise ValidationError

    class Meta:
        model = BoardBookmark
        fields = ['user', 'board', 'created_at', 'updated_at']