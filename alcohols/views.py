from django.shortcuts import render
from rest_framework import generics, permissions

from alcohols.models import AlcoholRecord
from alcohols.serializers import AlcoholRecordSerializers


class AlcoholRecordListAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = AlcoholRecordSerializers

    def get_queryset(self):
        return AlcoholRecord.objects.all()