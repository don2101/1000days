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
		

# @api_view(["GET"])
# def get_comments(request, diary_id):
# 	pass
# 	diary = None
# 	try:
# 		diary = Diary.objects.get(pk=diary_id)
# 	except Diary.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	if request.method == "GET":
# 		try:
# 			comments = diary.comment_set.all()
# 			serializer = CommentSerializer(data=comments, many=True)

# 			return Response(data=serializer.data, status=status.HTTP_200_OK)
# 		except:		# Response data에 comment_id 추가해야 함
# 			return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(["POST", "DELETE"])
# def comment(request, comment_id):
# 	if request.method == "POST":
# 		pass
# 	elif request.method == "DELETE":
# 		pass