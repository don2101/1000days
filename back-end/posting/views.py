from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import status

from .models import Diary, DiaryImage
from .serializers import DiarySerializer, DiaryImageSerializer, LikeSerializer

from account.serializers import UserProfileSerializer
from account.models import UserProfile
from account.account_service import get_user

from webtoken.token_service import check_login, check_user

# Create your views here.

User = get_user_model()

@api_view(["POST"])
def post_diary(request):
    # is_diary_open, selected_baby
    """
    diary를 작성하는 API
    ---
    ## POST headers
        Authorization: 글을 작성하는 유저의 jwt(String)
    ## POST body
        title: diary의 제목(String, Nullable)
        content: diary의 내용(String, Nullable)
        baby: baby의 id(Int)
        is_open: 공개 여부 설정(Boolean)
    ---
    """

    result = check_login(request.headers.get("Authorization"))
    
    if not result:
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    user = result

    serializer = DiarySerializer(data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save(writer=user)

        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def post_image(request, diary_id):
    """
    image를 diary에 연결하고 diary에 연결된 image를 조회하는 API
    ---
        POST: image를 upload하면 해당 diary_id를 가진 diary와 연결
        GET: diary_id를 가진 diary에 연결된 image의 url을 불러온다
    ## POST, GET parameter
        diary_id: diary의 id(Int)
    ##GET, POST headers
        Authorization: 업로드, 조회하는 유저의 jwt(String)
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
    result = check_login(request.headers.get("Authorization"))

    if not result:
        return Response(status=status.HTTP_403_FORBIDDEN)

    user = result

    diary = None

    try:
        diary = Diary.objects.get(pk=diary_id)
    except Diary.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "POST":

        if not check_user(user, diary.writer):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

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
            images = diary.diary_image.all()
            serializer = DiaryImageSerializer(images, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def user_diaries(request, account_name):
    """
    user가 작성한 모든 diary를 조회하는 API
    ---
    ## GET parameter
        account_name:  diary를 작성한 user의 nickname(String)
    ## GET headers
        Authorization: diary list를 조회하는 유저의 jwt(String)
    ## GET return body(List)
        id: diary의 id(Int)
        writer: 작성자의 nickname(String)
        title: diary의 제목(String)
        content: diary의 내용(String)
        baby: baby의 id(Int)
        created_at: 최초 작성 일자(Date)
        updated_at: 최근 수정 일자(Date)
        is_open: 공개 여부(Boolean)
        diary_image: diary에 연결된 image들의 url(List)
    ---
    """

    result = check_login(request.headers.get("Authorization"))

    if not result:
        return Response(status=status.HTTP_403_FORBIDDEN)

    user = get_user(account_name)

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
        id: diary의 id
        writer: 작성자의 nickname(String)
        title: diary의 제목(String)
        content: diary의 내용(String)
        baby: baby의 id(Int)
        created_at: 최초 작성 일자(Date)
        updated_at: 최근 수정 일자(Date)
        is_open: 공개 여부(Boolean)
        diary_image: diary에 연결된 image들의 url(List)
    ## GET, PUT, DELETE headers
        Authorization: diary를 조회, 수정, 삭제하는 유저의 jwt(String)
    ## PUT body
        title: diary의 제목(String)
        content: diary의 내용(String)
        baby: baby(Int)
    ---
    """
    result = check_login(request.headers.get("Authorization"))

    if not result:
        return Response(status=status.HTTP_403_FORBIDDEN)

    user = result

    diary = None

    try:
        diary = Diary.objects.get(pk=diary_id)
    except Diary.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == "GET":
        serializer = DiarySerializer(diary)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        if not check_user(user, diary.writer):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = DiarySerializer(diary, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # 이미지 수정도 추가
        
    elif request.method == "DELETE":
        if not check_user(user, diary.writer):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        diary.delete()

        return Response(status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def like(request, diary_id):
    """
    diary를 Like하고, diary에 like 누른 사람들을 조회하는 API
    ---
    ## GET, POST parameter
        diary_id: diary의 id(Int)
    ## Get return body
        like_user: 해당 글을 like한 유저의 nickname(List)
    ## GET, POST headers
        Authorization: like 하는 유저의 jwt(String)
    ---
    """
    result = check_login(request.headers.get("Authorization"))

    if not result:
        return Response(status=status.HTTP_403_FORBIDDEN)

    user = result

    diary = None
    
    try:
        diary = Diary.objects.get(pk=diary_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "POST":
        if user in diary.like_user.all():
            diary.like_user.remove(user)

        else:
            diary.like_user.add(user)

        return Response(status=status.HTTP_200_OK)

    elif request.method == "GET":
        serializer = LikeSerializer(diary)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def main_feed(request, account_name):
    """
    main feed에서 출력할 diary 요청 API
    ---
    ## GET parameter
        account_name: diary를 작성한 유저의 account_name
    ## GET headers
        Authorization: 유저의 jwt(String)
    ## Get return body
        like_user: 해당 글을 like한 유저의 nickname(List)
    ---
    """
    result = check_login(request.headers.get("Authorization"))

    if not result:
        return Response(status=status.HTTP_403_FORBIDDEN)

    user = get_user(account_name)

    posts = []
    
    for post in user.diary_set.all():
        posts.append(post)

    for follower in user.follower.all():
        for post in follower.user.diary_set.all():
            posts.append(post)

    posts = sorted(posts, key=lambda post: post.created_at, reverse=True)

    serializer = DiarySerializer(posts, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)
    
