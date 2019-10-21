from rest_framework import serializers
from .models import UserProfile, Baby
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'username']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['user', 'nickname', 'select_baby', 'account_open', 'follower_open']


class BabySerializer(serializers.ModelSerializer):
    parent = UserSerializer()
    
    class Meta:
        model = Baby
        fields = ['parent', 'name', 'birthday', 'spouse']


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.StringRelatedField(many=True)
    follower = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = UserProfile
        fields = ['following', 'follower']