from django.db import models
from django.conf import settings


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=45, null=False)
    select_baby = models.BooleanField(null=False)
    account_open = models.BooleanField(null=False)
    follower_open = models.BooleanField(null=False)


class Baby(models.Model):
    parent = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    birthday = models.DateField(null=False)
    spouse = models.CharField(max_length=45, null=True)
