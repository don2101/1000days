from django.shortcuts import render
from django.contrib.auth.hashers import make_password, is_password_usable

from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import status
from rest_framework_swagger import renderers

from .serializers import UserSerializer, UserProfileSerializer, BabySerializer
from .account_service import create_token, user_authenticate, set_password


# Create your views here.

@api_view(["POST"])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def signup(request):
    """
    회원 가입을 요청하는 API
    ---
    ## post parameter
        username: 사용자의 이름(String),
        password: 사용자의 비밀번호(String),
        email: 사용자의 email(String),
        nickname: 사용자의 계정 이름(String),
        select_baby: 아기 존재 여부(Boolean),
        account_open: 계정 정보 공개 여부(Boolean),
        follower_open: Follower 정보 공개 여부(Boolean)
    ---
    """
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
    '''
    로그인을 요청하는 API
    ---
    ## post parameter
        email: 사용자의 email(String),
        password: 사용자의 비밀번호(String),
    ---
    '''
    authenticated = user_authenticate(request.data["email"], request.data["password"])
    
    if authenticated:
        token = create_token(request.data)

        return Response(data={"token": token})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

