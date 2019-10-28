from django.contrib import admin
from .models import UserProfile, Baby, ProfileImage

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Baby)
admin.site.register(ProfileImage)
