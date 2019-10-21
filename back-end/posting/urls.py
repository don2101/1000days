from django.urls import path
from .views import post_diary, diary

urlpatterns = [
    path('diary/', post_diary, name="post_diary"),
    path('diary/<diary_id>', diary, name="diary"),
]