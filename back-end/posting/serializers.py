from rest_framework import serializers
from account.serializers import UserSerializer
from .models import Diary, DiaryImage


class DiarySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    diary_image = serializers.StringRelatedField()
    writer = serializers.StringRelatedField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Diary
        fields = ['id', 'writer', 'title', 'content', 'created_at', 'updated_at', 'diary_image']


class DiaryImageSerializer(serializers.ModelSerializer):
    diary = serializers.StringRelatedField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    thumb_nail = serializers.ImageField()

    class Meta:
        model = DiaryImage
        fields = ['diary', 'image', 'thumb_nail', 'created_at', 'updated_at']


class LikeSerializer(serializers.ModelSerializer):
    like_user = serializers.StringRelatedField(many=True)

    class Meta:
        model = Diary
        fields = ['like_user']
