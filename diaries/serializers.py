from rest_framework import serializers

from alcohols.models import AlcoholRecord
from alcohols.serializers import AlcoholRecordSerializers
from diaries.models import Diary


class DiarySerializers(serializers.ModelSerializer):
    alcohol_records = AlcoholRecordSerializers(many=True)

    class Meta:
        model = Diary

        fields = (
            'creator',
            'review',
            'date',
            'drunken_level',
            'hangover_level',
            'action_type',
            'alcohol_records',

        )

# class DiaryAPIView(ObjectMultipleModelAPIView):
#     querylist = [
#         {'queryset': Diary.objects.all(), 'serializer_class': DiarySerializers},
#         {'queryset': AlcoholRecord.objects.all(), 'serializer_class': AlcoholRecordSerializers},
#
#     ]
