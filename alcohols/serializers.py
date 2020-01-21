from rest_framework import serializers

from alcohols.models import AlcoholRecord


class AlcoholRecordSerializers(serializers.ModelSerializer):
    class Meta:
        model = AlcoholRecord
        fields = (
            'bottles',
            'glasses',
            'diary',
        )
