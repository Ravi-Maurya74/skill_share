from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

class UserManager(BaseUserManager):
    pass


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""

    firebase_uid = models.CharField(max_length=128, unique=True,primary_key=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # profile_pic = models.ImageField(
    #     null=True,
    #     blank=True,
    # )

    objects = BaseUserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "firebase_uid"