from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import status

from .models import UserProfile, Baby, ProfileImage
from webtoken.models import Blacklist
from .serializers import UserSerializer, UserProfileSerializer, BabySerializer, FollowSerializer, LikeSerializer, ProfileImageSerializer
from webtoken.serializers import BlacklistSerializer
from .account_service import user_authenticate, set_password
from webtoken.token_service import create_token, decode_token, check_login, check_user

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
        introduce: 사용자 소개 문구(String),
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


@api_view(["GET", "PUT", "DELETE"])
def personal(request, account_name):
    """
    개인 정보 열람, 수정 및 삭제를 요청하는 API
    ---
        GET: user의 개인 정보를 열람
        PUT: user의 개인 정보를 수정
        DELETE: user 삭제
    ## GET, PUT, DELETE parameter
        account_name: user의 nickname
    ## PUT body
        password: 사용자의 비밀번호(String),
        introduce: 사용자 소개 문구(String),
        nickname: 사용자의 계정 이름(String),
        select_baby: 아기 존재 여부(Boolean),
        account_open: 계정 정보 공개 여부(Boolean),
        follower_open: Follower 정보 공개 여부(Boolean),
    ## GET, PUT, DELETE headers
        Authorization: 사용자의 JWT(String)
    ## GET return body
        user: {
            email: 사용자의 email(String),
            username: 사용자의 이름(String)
        },
        nickname: 사용자의 계정 nickname(String),
        select_baby: baby 존재 여부(Boolean),
        account_open: 계정 존재 여부(Boolean),
        follower_open: Follower 정보 공개 여부(Boolean)
    ---
    """
    user_profile = None
    token_user = check_login(request.headers.get("Authorization"))
    if not token_user:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    try:
        user_profile = UserProfile.objects.get(nickname=account_name)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserProfileSerializer(user_profile)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        if not check_user(token_user, account_name):
	        return Response(status=status.HTTP_401_UNAUTHORIZED)
        user = user_profile.user
        try:
            user.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


    elif request.method == "PUT":
        if not check_user(token_user, account_name):
	        return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            serializer = UserProfileSerializer(user_profile, data=request.data, partial=True)
            
            if serializer.is_valid():
                instance = serializer.save()
                
                if request.data.get('password'):
                    user = instance.user

                    modified_data = set_password(request)
                    serializer = UserSerializer(user, data=modified_data, partial=True)

                    if serializer.is_valid():
                        serializer.save()

                        return Response(status=status.HTTP_202_ACCEPTED)

                    return Response(status=status.HTTP_404_NOT_FOUND)
                else:
                    return Response(status=status.HTTP_202_ACCEPTED)
            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST", "PUT"])
def babies(request, account_name):
    """
    baby의 정보 열람, 입력 및 수정을 요청하는 API
    ---
        GET: user의 nickname으로 계정을 찾고, 해당 계정 baby 정보를 출력
        POST: user의 nickname으로 계정을 찾고, 해당 계정 baby 정보를 입력
        PUT: user의 nickname으로 계정을 찾고, 해당 계정 baby 정보를 수정
    ## GET, POST, PUT parameter
        account_name: user의 nickname
    ## GET, PUT headers
        Authorization: 사용자의 JWT(String)
    ## POST body
        name: baby의 이름(String)
        birthday: 출생일(year-month-day)
        spouse: 배우자 이름(String)
    ## PUT body
        id: baby의 id(Integer)
        name: baby의 이름(String)
        birthday: 출생일(year-month-day)
        spouse: 배우자 이름(String)
    ## GET return body
        id: baby의 id(Integer)
        name: baby의 이름(String)
        birthday: 출생일(year-month-day)
        spouse: 배우자 이름(String)
    ---
    """
    if request.method == "GET":
        token_user = check_login(request.headers.get("Authorization"))
        if not token_user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

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

    elif request.method == "PUT":
        token_user = check_login(request.headers.get("Authorization"))
        user = token_user

        baby = user.baby_set.get(id=request.data['id'])
        
        try:
            serializer = BabySerializer(baby, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()

                return Response(status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except UserProfile.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def follow(request, account_name):
    """
    follow 열람, 입력을 수행 하는 API
    ---
        GET: user의 nickname으로 계정을 찾고, 해당 계정 follow 정보를 출력
        POST: user의 nickname으로 계정을 찾고, 해당 계정에 follow 정보를 추가
        (following: 유저가 follow 하는 사람, follower: 유저를 follow 하는 사람)
    ## GET, POST parameter
        account_name: user의 nickname
    ## GET, POST headers
        Authorization: 사용자의 JWT(String)
    ## POST body
        follow: follow 할 사람의 nickname(String)
    ## GET return body
        following: 유저가 follow 하는 사람의 목록(List)
        follower: 유저를 follow 하는 사람의 목록(List)
    ---
    """
    token_user = check_login(request.headers.get("Authorization"))
    if not token_user:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "GET":
        try:
            user_profile = UserProfile.objects.get(nickname=account_name)
            
            serializer = FollowSerializer(user_profile)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        except UserProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == "POST":
        if not check_user(token_user, account_name):
	        return Response(status=status.HTTP_401_UNAUTHORIZED)
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
    ## POST headers
        Authorization: 사용자가 로그인할 때 받은 JWT(String)
    ---
    '''
    token = decode_token(request.headers.get("Authorization"))
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
    ## POST headers
        Authorization: 사용자의 JWT(String)
    ## POST body
        password: 사용자의 비밀번호(String)
    ---
    '''
    token = decode_token(request.headers.get("Authorization"))
    if token:
        authenticated = user_authenticate(token.get("email"), request.data["password"])
        if authenticated:
            return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(["GET", "POST", "PUT", "DELETE"])
def profile_image(request, account_name):
    """
    User 프로필 사진 열람, 생성, 수정, 삭제를 요청하는 API
    ---
    ## GET, POST, PUT, DELETE parameter
        account_name: user의 nickname
    ## GET, POST, PUT, DELETE headers
        Authorization: 사용자의 JWT(String)
    ## POST, PUT body
        image: 프로필 이미지로 사용할 사진(File)
    ## GET return body
        image: 프로필 이미지의 url(String)
    ---
    """
    user = None
    token_user = check_login(request.headers.get("Authorization"))
    if not token_user:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    user = token_user
        
    if request.method == "GET":
        image = None
        
        try:
            image = user.profile_image
        except ProfileImage.DoesNotExist:
            return Response(data={"user":account_name, "image": None, "thumb_nail": None}, status=status.HTTP_200_OK)

        serializer = ProfileImageSerializer(image)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        if not check_user(token_user, account_name):
	        return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = ProfileImageSerializer(data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save(user=user)

            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        if not check_user(token_user, account_name):
	        return Response(status=status.HTTP_401_UNAUTHORIZED)
        image = None
        
        try:
            image = user.profile_image
        except ProfileImage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProfileImageSerializer(image, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        image = None

        try:
            image = user.profile_image

            image.delete()

            return Response(status=status.HTTP_202_ACCEPTED)

        except ProfileImage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def getusers(request):
    """
    유저 검색 API
    ---
    ## POST headers
        Authorization: 사용자의 JWT(String)
    ## POST body
        text: nickname 검색할 문자열(String)
    ## Get return body
        user: 사용자의 닉네임(String)
        image: 프로필 이미지의 url(String)
        thumb_nail: 사용자의 썸네일(String)
    ---
    """
    token_user = check_login(request.headers.get("Authorization"))
    if not token_user:
	    return Response(status=status.HTTP_401_UNAUTHORIZED)

    text = request.data["text"]

    try:
        userprofiles=UserProfile.objects.filter(nickname__icontains=text)
        user=userprofiles
        result = []
        for userprofile in userprofiles:
            try:
                profileimage = userprofile.user.profile_image
                serializer = ProfileImageSerializer(profileimage)
                result.append(serializer.data)
            except ProfileImage.DoesNotExist:
                result.append({"user": userprofile.nickname, "image": "", "thumb_nail": ""})
        return Response(data=result, status=status.HTTP_200_OK)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)