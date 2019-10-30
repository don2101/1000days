from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import status

from .models import Diary, DiaryImage
from .serializers import DiarySerializer, DiaryImageSerializer, LikeSerializer

from account.serializers import UserProfileSerializer
from account.models import UserProfile

from webtoken.token_service import decode_token, check_user

# Create your views here.

User = get_user_model()

@api_view(["POST"])
def post_diary(request):
    """
    diary를 작성하는 API
    ---
    ## POST body
        title: diary의 제목(String, Nullable)
        content: diary의 내용(String, Nullable)
        token: 유저 인증 jwt(String)
    ---
    """
    token = request.data['token']
    decoded_token = decode_token(token)

    if not decoded_token:
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    user = User.objects.get(email=decoded_token['email'])

    if not user:
        return Response(status=status.HTTP_403_FORBIDDEN)

    serializer = DiarySerializer(data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save(writer=user)

        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def post_image(request, diary_id):
    """
    image를 작성하고 조회하는 API
    ---
        POST: image를 upload하면 해당 diary_id를 가진 diary와 연결
        GET: diary_id를 가진 diary에 연결된 image의 url을 불러온다
    ## POST, GET parameter
        diary_id: diary의 id(Int)

    ## POST body
        image: 이미지 파일(File)

    ## Get return body
        diary: 연결된 idary(String)
        image: image의 url(String)
        thumb_nail: thumbnail의 url(String)
        created_at: 최초 upload 일시(Date)
        updated_at: 최근 수정 일시(Date)
    ---
    """
    if request.method == "POST":
        try:
            diary = Diary.objects.get(pk=diary_id)
        except Diary.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        try:
            serializer = DiaryImageSerializer(data=request.data, partial=True)
            
            if serializer.is_valid():
                
                serializer.save(diary=diary)

                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
        except Exception:
            Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "GET":
        try:
            diary = Diary.objects.get(pk=diary_id)
        except Diary.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            images = diary.diaryimage_set.all()
            serializer = DiaryImageSerializer(images, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def user_diaries(request, account_name):
    """
    해당 user가 작성한 모든 diary를 조회하는 API
    ---
    ## GET parameter
        account_name: user의 nickname(String)

    ## Get return body(List)
        id: diary의 id(Int)
        writer: 작성자의 nickname(String)
        title: diary의 제목(String)
        content: diary의 내용(String)
        created_at: 최초 작성 일자(Date)
        updated_at: 최근 수정 일자(Date)
    ---
    """
    try:
        user = UserProfile.objects.get(nickname=account_name).user
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        diaries = user.diary_set.all()
        serializer = DiarySerializer(diaries, many=True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def diary(request, diary_id):
    """
    diary에 대해 조회, 수정, 삭제를 요청하는 API
    ---
    ## GET, PUT, DELETE parameter
        diary_id: diary의 id(Int)

    ## Get return body
        writer: 작성자의 nickname(String)
        title: diary의 제목(String)
        content: diary의 내용(String)
        created_at: 최초 작성 일자(Date)
        updated_at: 최근 수정 일자(Date)

    ## PUT body
        title: diary의 제목(String)
        content: diary의 내용(String)
        token: 유저 인증 jwt(String)

    ## DELETE body
        token: 유저 인증 jwt(String)
    ---
    """
    diary = None

    try:
        diary = Diary.objects.get(pk=diary_id)
    except Diary.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == "GET":
        serializer = DiarySerializer(diary)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        token = request.data['token']

        if not check_user(diary.writer, token):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = DiarySerializer(diary, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # 이미지 수정도 추가
        
    elif request.method == "DELETE":
        token = request.data['token']

        if not check_user(diary.writer, token):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        diary.delete()

        return Response(status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def like(request, diary_id):
    """
    diary를 Like하고 조회하는 API
    ---
    ## GET, POST parameter
        diary_id: diary의 id(Int)

    ## Get return body
        like_user: 해당 글을 like한 유저의 nickname(List)

    ## POST body
        nickname: 해당 글을 like하는 유저의 nickname(String)
    ---
    """
    diary = None
    
    try:
        diary = Diary.objects.get(pk=diary_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "POST":
        user = None
        
        try:
            user = UserProfile.objects.get(nickname=request.data['nickname']).user
        except UserProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if user in diary.like_user.all():
            diary.like_user.remove(user)

            return Response(status=status.HTTP_200_OK)
        else:
            diary.like_user.add(user)

            return Response(status=status.HTTP_200_OK)

    elif request.method == "GET":
        serializer = LikeSerializer(diary)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def main_feed(request, account_name):
    user = None
    
    try:
        user = UserProfile.objects.get(nickname=account_name).user
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # if not check_user(user, request.data['token']):
    #     return Response(status=status.HTTP_403_FORBIDDEN)

    posts = []
    
    for post in user.diary_set.all():
        posts.append(post)


    for follower in user.follower.all():
        for post in follower.user.diary_set.all():
            posts.append(post)

    posts = sorted(posts, key=lambda post: post.created_at, reverse=True)

    serializer = DiarySerializer(posts, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)
    
