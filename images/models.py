from django.db import models
from diaries.models import Diary
from users.models import User
from utils.django.models import TimeStampedModel


class Image(TimeStampedModel):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='creator')
    main_image = models.ImageField('메인 이미지', blank=True, upload_to="image_photos")
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE, null=True,related_name='diary')
    is_main = models.BooleanField(default=True)

