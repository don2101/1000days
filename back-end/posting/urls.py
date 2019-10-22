from django.urls import path
from .views import post_diary, diary

urlpatterns = [
    path('', post_diary, name="post_diary"),
    path('<diary_id>', diary, name="diary"),
]