from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import status

from .models import UserProfile, Baby
from .serializers import UserSerializer, UserProfileSerializer, BabySerializer
from .account_service import create_token, user_authenticate, set_password

User = get_user_model()

# Create your views here.

@api_view(["POST"])
def signup(request):
    """
    회원 가입을 요청하는 API
    ---
    ## POST parameter
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
        return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    '''
    로그인을 요청하는 API
    ---
    ## POST parameter
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


@api_view(["GET"])
def personal(request, account_name):
    """
    개인 정보를 요청하는 API
    ---
    user의 nickname으로 계정을 찾아 정보를 return
    
    ## Get return
        user: {
            email: 사용자의 email(String),
            username: 사용자의 이름(String)
        },
        nickname: 사용자의 계정 이름(String),
        select_baby: baby 존재 여부(Boolean),
        account_open: 계정 존재 여부(Boolean),
        follower_open: Follower 정보 공개 여부(Boolean)
    ---
    """
    try:
        user_profile = UserProfile.objects.get(nickname=account_name)
        serializer = UserProfileSerializer(user_profile)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", "POST"])
def babies(request, account_name):
    """
    baby의 정보를 입력하는 API
    ---
        GET: user의 nickname으로 계정을 찾아 정보를 return
        POST: user의 nickname으로 계정을 찾고, 해당 계정에 baby 정보를 입력
    ## POST parameter
        name: baby의 이름(String)
        birthday: 출생일(year-month-day)
        spouse: 배우자 이름(String)

    ## Get return
        name: baby의 이름(String)
        birthday: 출생일(year-month-day)
        spouse: 배우자 이름(String)
    ---
    """
    # 모든 baby 출력
    if request.method == "GET":
        
        try:
            user_profile = UserProfile.objects.get(nickname=account_name)
            user = user_profile.user
            
            babies = user.baby_set.all()
            serializer = BabySerializer(babies, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
            
        except UserProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == "POST":
        try:
            user_profile = UserProfile.objects.get(nickname=account_name)
            user = user_profile.user
            
            serializer = BabySerializer(data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save(parent=user)

                return Response(status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except UserProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
