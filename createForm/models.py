from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL # auth.User

# Create your models here.



class DataType(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    parent_id = models.ForeignKey('self',on_delete=models.CASCADE,null=True,related_name='children')
    name = models.CharField(max_length=264)
    slug = models.CharField(max_length=264)

class Attribute(models.Model):
    name = models.CharField(max_length=264)
    slug = models.CharField(max_length=264)

class DataAttribute(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    dataType = models.ForeignKey(DataType,on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=264)
    slug = models.CharField(max_length=264)
    use_in_children = models.BooleanField(default=0)






