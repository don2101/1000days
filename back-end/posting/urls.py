from django.urls import path
from .views import post_diary, diary, post_image

urlpatterns = [
    path('', post_diary, name="post_diary"),
    path('<int:diary_id>/images/', post_image, name="post_image"),
    path('<int:diary_id>', diary, name="diary"),
]