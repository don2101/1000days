from rest_framework import serializers
from django.conf import settings
from .models import UserProfile, Baby


class UserSerializer(serializers.ModelSerializer):
    user = settings.AUTH_USER_MODEL

    class Meta:
        model = UserProfile
        fields = ['user', 'nickname', 'select_baby', 'account_open', 'follower_open']


class BabySerializer(serializers.ModelSerializer):
    parent = settings.AUTH_USER_MODEL
    
    class Meta:
        model = Baby
        fields = ['name', 'birthday', 'spouse']