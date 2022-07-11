from rest_framework import serializers

from communityapp.models import BoardCategory


class BoardCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardCategory
        fields = ['kind', 'description']
