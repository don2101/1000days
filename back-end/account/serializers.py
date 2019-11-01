from rest_framework import serializers
from .models import UserProfile, Baby, ProfileImage
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'username']


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = UserProfile
        fields = ['user', 'nickname', 'introduce', 'select_baby', 'account_open', 'follower_open']


class BabySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    parent = serializers.StringRelatedField()
    
    class Meta:
        model = Baby
        fields = ['id', 'parent', 'name', 'birthday', 'spouse']


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.StringRelatedField(many=True)
    follower = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = UserProfile
        fields = ['following', 'follower']


class LikeSerializer(serializers.ModelSerializer):
    likes = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['likes']


class ProfileImageSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    thumb_nail = serializers.ImageField()

    class Meta:
        model = ProfileImage
        fields = ['user', 'image', 'thumb_nail']
