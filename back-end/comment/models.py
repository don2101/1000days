from django.db import models
from django.conf import settings
from posting.models import Diary

# Create your models here.
class Comment(models.Model):
	writer = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
	diary = models.ForeignKey(Diary, null=False, on_delete=models.CASCADE)
	content = models.CharField(max_length=100, null=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)