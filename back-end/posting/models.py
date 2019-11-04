from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFit

from account.models import Baby


# Create your models here.
class Diary(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes')
    baby = models.ForeignKey(Baby, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class DiaryImage(models.Model):
    diary = models.ForeignKey(Diary, null=False, on_delete=models.CASCADE, related_name='diary_image')
    image = models.ImageField(
        upload_to="images/" + "%Y%m%d%h"
    )
    thumb_nail = ImageSpecField(
        source='image',
        processors=[ResizeToFit(width=320, upscale=False)],
        options={'quality': 60}
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image
