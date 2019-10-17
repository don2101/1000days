from django.shortcuts import render
from django.contrib.auth.hashers import make_password, is_password_usable
from django.http import QueryDict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import UserSerializer, UserProfileSerializer, BabySerializer

# Create your views here.

@api_view(["POST"])
def signup(request):
    # querydict is immutable. convert it to dict and update password, then recover it back to querydict
    request_dict = request.data.dict()
    request_dict['password'] = make_password(request.data['password'])
    modified_data = QueryDict('', mutable=True)
    modified_data.update(request_dict)

    user_serializer = UserSerializer(data=modified_data, partial=True)
    
    if user_serializer.is_valid():
        user_instance = user_serializer.save()
        
        profile_serializer = UserProfileSerializer(data=request.data, partial=True)
        
        if profile_serializer.is_valid():
            profile_instance = profile_serializer.save(user=user_instance)


def login(request):
    pass


def logout(request):
    pass

