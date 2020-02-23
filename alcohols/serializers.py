from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from alcohols.models import AlcoholRecord


class AlcoholRecordSerializers(serializers.ModelSerializer):
    def validate(self, attrs):
        if not attrs.get('bottles') and not attrs.get('glasses'):
            raise ValidationError("병이나 잔 중에 최소 하나는 입력해야 합나다.")
        return attrs

    class Meta:
        model = AlcoholRecord
        fields = (
            'bottles',
            'glasses',
            'diary',
        )
