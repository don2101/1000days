from rest_framework import serializers
from django.conf import settings
from .models import Blacklist

class BlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blacklist
        fields = ['email', 'exp']