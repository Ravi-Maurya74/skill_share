from django.db import models


class User(models.Model):
    firebase_uid = models.CharField(max_length=128, unique=True,primary_key=True)
    name = models.CharField(max_length=255,blank=False,null=False)
    city = models.CharField(max_length=255,blank=False,null=False)
    profile_pic = models.TextField()
