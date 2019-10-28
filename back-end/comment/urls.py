from django.urls import path
from .views import post_comment, get_comments, update_comment, delete_comment

urlpatterns = [
	path('', post_comment, name="post_comment"),
	path('getcomments/', get_comments, name="get_comments"),
	path('updatecomment/', update_comment, name="update_comment"),
	path('deletecomment/', delete_comment, name="delete_comment")
]