from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=45, null=False, unique=True)
    select_baby = models.BooleanField(null=False)
    account_open = models.BooleanField(null=False)
    follower_open = models.BooleanField(null=False)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="following")
    follower = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="follower")
    

class Baby(models.Model):
    parent = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=45, null=False)
    birthday = models.DateField(null=False)
    spouse = models.CharField(max_length=45, null=True)


def get_nickname(self):
    return self.userprofile.nickname

User.add_to_class("__str__", get_nickname)