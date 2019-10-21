from django.shortcuts import render
from django.contrib.auth.hashers import make_password, is_password_usable

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import UserSerializer, UserProfileSerializer, BabySerializer
from .account_service import create_token, user_authenticate, set_password, decode_token
from .models import Blacklist


# Create your views here.

@api_view(["POST"])
def signup(request):
    modified_data = set_password(request)    
    
    user_serializer = UserSerializer(data=modified_data, partial=True)
    
    if user_serializer.is_valid():
        user_instance = user_serializer.save()
        
        profile_serializer = UserProfileSerializer(data=request.data, partial=True)
        
        if profile_serializer.is_valid():
            profile_instance = profile_serializer.save(user=user_instance)

            return Response(status=status.HTTP_201_CREATED)
        return Response(profile_serializer.error,status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(user_serializer.error, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    authenticated = user_authenticate(request.data["email"], request.data["password"])
    
    if authenticated:
        # blacklist = Blacklist.objects.get(email=request.data["email"])            이것도 나중에 수정.
        # if blacklist:
        #     blacklist.delete()
        token = create_token(request.data)

        return Response(data={"token": token})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def logout(request):
    token = decode_token(request.data["token"])
    print(token)
    # blacklist = Blacklist.objects.create(email=token.get("email"), expiry_date=token.get("exp"))

    return Response(status=status.HTTP_200_OK)