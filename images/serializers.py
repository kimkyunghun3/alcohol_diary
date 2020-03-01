from rest_framework import serializers
from images.models import Image


class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'creator',
            'main_image',
            'is_main',
        )
