from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=264)
    country_key = models.CharField(max_length=264)


class Province(models.Model):
    name = models.CharField(max_length=264)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    code = models.CharField(max_length=264,null=True)
    short_code = models.CharField(max_length=264,null=True)
    status = models.BooleanField(default=1)

class County(models.Model):
    name = models.CharField(max_length=264)
    province = models.ForeignKey(Province,on_delete=models.CASCADE)
    code = models.CharField(max_length=264,null=True)
    short_code = models.CharField(max_length=264,null=True)
    status = models.BooleanField(default=1)


class RuralDistrict(models.Model):
    name = models.CharField(max_length=264)
    province = models.ForeignKey(Province,on_delete=models.CASCADE)
    county = models.ForeignKey(County,on_delete=models.CASCADE)
    code = models.CharField(max_length=264,null=True)
    sector_id = models.CharField(max_length=264,null=True)
    short_code = models.CharField(max_length=264,null=True)
    status = models.BooleanField(default=1)

class City(models.Model):
    name = models.CharField(max_length=264)
    province = models.ForeignKey(Province,on_delete=models.CASCADE)
    county = models.ForeignKey(County,on_delete=models.CASCADE)
    code = models.CharField(max_length=264,null=True)
    sector_id = models.CharField(max_length=264,null=True)
    short_code = models.CharField(max_length=264,null=True)
    status = models.BooleanField(default=1)


