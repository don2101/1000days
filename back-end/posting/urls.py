from django.urls import path
from .views import post_diary, diary, post_image, user_diaries, like, main_feed

urlpatterns = [
    path('', post_diary, name="post_diary"),
    path('<int:diary_id>/images/', post_image, name="post_image"),
    path('<int:diary_id>/', diary, name="diary"),
    path('<str:account_name>/', user_diaries, name="diaries"),
    path('<str:account_name>/main/', main_feed, name="main_feed"),
    path('<int:diary_id>/likes/', like, name="like")
]