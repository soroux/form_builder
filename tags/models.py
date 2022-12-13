from django.conf import settings
from django.db import models

# Create your models here.
User = settings.AUTH_USER_MODEL # auth.User


class Tag(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=264)
    slug = models.CharField(max_length=264)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
