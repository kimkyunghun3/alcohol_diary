from rest_framework import serializers

from users.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'img_profile',
        )


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (

            'img_profile',
        )

    def to_representation(self, instance):
        return UserSerializers(instance).data
