from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    name = models.CharField(max_length=30)
    img_profile = models.ImageField('프로필 이미지', blank=True, upload_to='profile')
    username_pk = models.UUIDField()

