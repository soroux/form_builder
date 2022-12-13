from django.conf import settings
from django.db import models

from createForm.models import UserEntry, DataType, DataAttribute

User = settings.AUTH_USER_MODEL  # auth.User

# Create your models here.
class RawData(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    user_entry = models.ForeignKey(UserEntry,on_delete=models.CASCADE)
    dataType = models.ForeignKey(DataType,on_delete=models.CASCADE)
    dataAttribute = models.ForeignKey(DataAttribute,on_delete=models.CASCADE)
    data = models.CharField(max_length=264)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
