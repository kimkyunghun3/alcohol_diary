from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from alcohols.models import AlcoholRecord, AlcoholType, Alcohol


class AlcoholTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlcoholType
        fields = (
            'alcohol_name',
        )


class AlcoholSerializer(serializers.ModelSerializer):
    alcohol_type = AlcoholTypeSerializer()

    class Meta:
        model = Alcohol
        fields = (
            'alcohol_type',
            'name',
        )

class AlcoholRecordCreateSerializers(serializers.ModelSerializer):
    def validate(self, attrs):
        if not attrs.get('bottles') and not attrs.get('glasses'):
            raise ValidationError("병이나 잔 중에 최소 하나는 입력해야 합나다.")
        return attrs

    class Meta:
        model = AlcoholRecord
        fields = (
            'bottles',
            'glasses',

            'alcohol_type',
            'alcohol_name',
        )



class AlcoholRecordSerializers(serializers.ModelSerializer):
    alcohol_type = serializers.CharField(source='alcohol.name')
    alcohol_name = serializers.CharField(source='alcohol.alcohol_type.alcohol_name')

    class Meta:
        model = AlcoholRecord
        fields = (
            'bottles',
            'glasses',

            'alcohol_type',
            'alcohol_name',
        )
