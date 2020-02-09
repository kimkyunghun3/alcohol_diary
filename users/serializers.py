from rest_framework import serializers

from users.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'name',
            'img_profile',
            'id',
        )


class UserOnlySerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'name',
            'img_profile',

        )
