from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    username_pk = models.CharField(max_length=30)
    img_profile = models.ImageField('프로필 이미지', blank=True, upload_to='profile')


