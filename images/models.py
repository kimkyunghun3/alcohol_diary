from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=30, null=True)
    main_image = models.ImageField('메인 이미지', blank=True, upload_to="image_photos")

    def __str__(self):
        return self.name
