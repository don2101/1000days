from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import status

from .models import Comment
from account.models import UserProfile
from posting.models import Diary
from .serializers import CommentSerializer
from account.serializers import UserProfileSerializer
from posting.serializers import DiarySerializer

from webtoken.token_service import decode_token, check_user

# Create your views here.
User = get_user_model()

@api_view(["POST"])
def post_comment(request):
	"""
    댓글 작성을 요청하는 API
    ---
    token, content, diary_id를 받아 status을 return
    ## POST parameter
        token: 사용자의 token(String),
		content: 사용자가 작성하고자 하는 댓글 내용
        diary_id: 사용자가 댓글을 달고자 하는 Diary의 id
    ## Get return
        status: 결과
    ---
    """
	diary_id = request.data["diary_id"]
	token = request.data['token']

	decoded_token = decode_token(token)
	if not decoded_token:
		return Response(status=status.HTTP_403_FORBIDDEN)

	try:
		user = User.objects.get(email = decoded_token["email"])
		print(user)
		print(type(user))
	except User.DoesNotExist:
		return Response(status = status.HTTP_403_FORBIDDEN)

	try:
		diary = Diary.objects.get(pk = diary_id)
		print(diary)
		print(type(diary))
	except Diary.DoesNotExist:
		return Response(status=status.HTTP_400_BAD_REQUEST)
	
	serializer = CommentSerializer(data={"content": request.data["content"]}, partial=True)
	if serializer.is_valid():
		serializer.save(writer=user, diary=diary)

		return Response(status=status.HTTP_201_CREATED)
	return Response(status=status.HTTP_400_BAD_REQUEST)
		

@api_view(["POST"])
def get_comments(request):
	"""
    해당 게시글의 모든 댓글을 조회하는 API
    ---
    diary_id를 받아 comment와 status을 return
    ## POST parameter
        diary_id: 사용자가 댓글을 조회하고자 하는 Diary의 id
    ## Get return body
		id: comment의 id(Int)
		writer: 작성자의 nickname(String)
        diary: 댓글을 작성한 diary의 제목(String)
        content: comment의 내용(String)
        created_at: 최초 작성 일자(Date)
        updated_at: 최근 수정 일자(Date)
    ---
    """
	diary_id=request.data["diary_id"]
	try:
		diary = Diary.objects.get(pk=diary_id)
	except Diary.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	try:
		comments = diary.comment_set.all()
		serializer = CommentSerializer(comments, many=True)

		return Response(data=serializer.data, status=status.HTTP_200_OK)
	except:
		return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(["POST", "DELETE"])
# def comment(request, comment_id):
# 	if request.method == "POST":
# 		pass
# 	elif request.method == "DELETE":
# 		pass