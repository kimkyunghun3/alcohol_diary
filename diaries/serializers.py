from rest_framework import serializers

from diaries.models import Diary


class DiarySerializers(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = (
            'creator',
            'review',
            'date',
            'drunken_level',
            'hangover_level',
            'action_type',
        )
