from rest_framework import serializers
from django.conf import settings
from .models import UserProfile, Baby, Blacklist
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'username']


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = UserProfile
        fields = ['user', 'nickname', 'select_baby', 'account_open', 'follower_open']


class BabySerializer(serializers.ModelSerializer):
    parent = serializers.StringRelatedField()
    
    class Meta:
        model = Baby
        fields = ['parent', 'name', 'birthday', 'spouse']


class BlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blacklist
        fields = ['email', 'exp']