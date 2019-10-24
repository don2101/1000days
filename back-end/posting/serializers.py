from rest_framework import serializers
from account.serializers import UserSerializer
from .models import Diary, DiaryImage


class DiarySerializer(serializers.ModelSerializer):
    # 관계를 어떻게 표현하느냐의 차이, 입력을 받아들이는 데는 상관이 없다.
    # 그것은 model에서의 문제
    writer = serializers.StringRelatedField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Diary
        fields = ['writer', 'title', 'content', 'created_at', 'updated_at']


class DiaryImageSerializer(serializers.ModelSerializer):
    diary = serializers.StringRelatedField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    thumb_nail = serializers.ImageField()

    class Meta:
        model = DiaryImage
        fields = ['diary', 'image', 'thumb_nail', 'created_at', 'updated_at']
