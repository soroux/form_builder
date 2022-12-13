from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL  # auth.User


# Create your models here.


class LimitEntry(models.Model):
    name = models.CharField(max_length=264)



class DataType(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    user_entry = models.ManyToManyField(User,through="UserEntry",related_name="dataTypes_entry")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='children')
    name = models.CharField(max_length=264)
    slug = models.CharField(max_length=264)
    limit_entry = models.ForeignKey(LimitEntry,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_first_parent(self):
        if self.parent is not None:
            return False
        return True

class UserEntry(models.Model):
    dataType = models.ForeignKey(DataType,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Attribute(models.Model):
    name = models.CharField(max_length=264)
    fa_name = models.CharField(max_length=264)
    min = models.BooleanField(default=False)
    max = models.BooleanField(default=False)
    default = models.BooleanField(default=False)
    max_length = models.BooleanField(default=False)
    min_length = models.BooleanField(default=False)


class DataAttribute(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    dataType = models.ForeignKey(DataType, on_delete=models.CASCADE, related_name='dataAttributes')
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    name = models.CharField(max_length=264)
    slug = models.CharField(max_length=264)
    order = models.IntegerField(default=1)
    min = models.IntegerField(null=True)
    max = models.IntegerField(null=True)
    min_length = models.IntegerField(null=True)
    max_length = models.IntegerField(null=True)
    default = models.CharField(max_length=264, null=True)
    use_in_children = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
