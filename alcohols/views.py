from django.shortcuts import render
from rest_framework import generics, permissions

from alcohols.models import AlcoholRecord, Alcohol, AlcoholType
from alcohols.serializers import AlcoholRecordSerializers, AlcoholTypeSerializers, AlcoholSerializers


class AlcoholRecordListAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = AlcoholRecordSerializers,AlcoholSerializers,AlcoholTypeSerializers

    def get_queryset(self):
        return AlcoholRecord.objects.all(), Alcohol.objects.all(), AlcoholType.objects.all()