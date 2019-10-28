from django.urls import path
from .views import post_comment, get_comments#, comment

urlpatterns = [
	path('', post_comment, name="post_comment"),
	path('getcomments/', get_comments, name="get_comments"),
	# path('<int:comment_id>/', comment, name="comment")
]