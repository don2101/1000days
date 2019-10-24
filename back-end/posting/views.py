from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import status

from .models import Diary, DiaryImage
from .serializers import DiarySerializer, DiaryImageSerializer

from account.serializers import UserProfileSerializer
from account.models import UserProfile

from webtoken.token_service import decode_token, check_user

# Create your views here.

User = get_user_model()

@api_view(["POST"])
def post_diary(request):
    token = request.data['token']
    decoded_token = decode_token(token)

    if not decoded_token:
        return Response(status=status.HTTP_403_FORBIDDEN)
    
    user = User.objects.get(email=decoded_token['email'])

    if not user:
        return Response(status=status.HTTP_403_FORBIDDEN)

    # 부분적으로 이름이 일치하는 column에 대해 입력
    serializer = DiarySerializer(data=request.data, partial=True)

    if serializer.is_valid():
        # 객체를 직접 연결 => model에서 처리하는 로직
        serializer.save(writer=user)

        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def post_image(request, diary_id):
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
    print(account_name)
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


