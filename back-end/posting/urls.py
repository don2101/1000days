from django.urls import path
from .views import post_diary, diary, post_image

urlpatterns = [
    path('', post_diary, name="post_diary"),
    path('<diary_id>', diary, name="diary"),
    path('<diary_id>/images/', post_image, name="post_image"),
]