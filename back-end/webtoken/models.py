from django.db import models

# Create your models here.
class Blacklist(models.Model):
    email = models.CharField(max_length=45, null=False)
    expiry_date = models.DateTimeField(null=False)