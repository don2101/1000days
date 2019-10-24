from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import status

from .models import UserProfile, Baby
from webtoken.models import Blacklist
from .serializers import UserSerializer, UserProfileSerializer, BabySerializer, FollowSerializer
from webtoken.serializers import BlacklistSerializer
from .account_service import user_authenticate, set_password
from webtoken.token_service import create_token, decode_token

from datetime import timezone, datetime

User = get_user_model()

# Create your views here.

@api_view(["POST"])
def signup(request):
    """
    회원 가입을 요청하는 API
    ---
    ## POST body
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
        else:
            userprofile = UserProfile.objects.get(email = request.data["email"])
            userprofile.delete()
            return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    """
    로그인을 요청하는 API
    ---
    이메일, 비밀번호를 받아 JWT과 nickname을 return
    ## POST body
        email: 사용자의 email(String),
        password: 사용자의 비밀번호(String),
    ## GET return body
        token: {
            email: 사용자의 email(String),
            exp: token의 만료기한(int)
        },
        nickname: 사용자의 계정 이름(String),
    ---
    token은 변조되어 있음.
    """
    authenticated = user_authenticate(request.data["email"], request.data["password"])
    
    if authenticated:
        blacklist = Blacklist.objects.filter(email=request.data["email"])
        if blacklist:
            blacklist.delete()
        token = create_token(request.data)
        userprofile = UserProfile.objects.get(user__email=request.data["email"])
        
        return Response(data={"token": token, "nickname": userprofile.nickname})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def personal(request, account_name):
    """
    개인 정보를 요청하는 API
    ---
    user의 nickname으로 계정을 찾아 정보를 return

    ## GET parameter
        account_name: user의 nickname
    
    ## GET return body
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

    ## GET, POST parameter
        account_name: user의 nickname
    
    ## POST body
        name: baby의 이름(String)
        birthday: 출생일(year-month-day)
        spouse: 배우자 이름(String)

    ## Get return body
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


@api_view(["GET", "POST"])
def follow(request, account_name):
    """
    follow 기능을 수행 하는 API
    ---
        GET: user의 nickname으로 계정을 찾아 follower, following에 대한 정보 return
        POST: user의 nickname으로 계정을 찾고, 해당 계정에 follow 정보를 추가
        (following: 유저가 follow 하는 사람, follower: 유저를 follow 하는 사람)

    ## GET, POST parameter
        account_name: user의 nickname
    
    ## POST body
        follow: follow 할 사람의 nickname(String)

    ## Get return body
        following: 유저가 follow 하는 사람의 목록(List)
        follower: 유저를 follow 하는 사람의 목록(List)
    ---
    """
    if request.method == "GET":
        try:
            user_profile = UserProfile.objects.get(nickname=account_name)

            serializer = FollowSerializer(user_profile)
            print(serializer.data)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        except UserProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    elif request.method == "POST":
        try:
            user_profile = UserProfile.objects.get(nickname=account_name)
            following_user = UserProfile.objects.get(nickname=request.data['follow'])

            if following_user in user_profile.following.all():
                user_profile.following.remove(following_user.user)
                following_user.follower.remove(user_profile.user)
            
            else:
                user_profile.following.add(following_user.user)
                following_user.follower.add(user_profile.user)

            return Response(status=status.HTTP_200_OK)
            
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def logout(request):
    '''
    로그아웃을 요청하는 API
    ---
    ## POST body
        token: 사용자가 로그인할 때 받은 JWT(String),
    ---
    '''
    token = decode_token(request.data["token"])
    email = token.get("email")
    expiry_date = datetime.fromtimestamp(token.get("exp"), timezone.utc)
    blacklist_serializer = BlacklistSerializer(data={"email": email, "expiry_date": expiry_date})

    if blacklist_serializer.is_valid():
        blacklist_serializer.save()
    
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(blacklist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def authuser(request):
    '''
    Mypage 입장허가를 요청하는 API
    ---
    ## POST body
        token: 사용자의 JWT(String)
        password: 사용자의 비밀번호(String),
    ---
    '''
    token = decode_token(request.data["token"])
    if token:
        authenticated = user_authenticate(token.get("email"), request.data["password"])
        if authenticated:
            return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)