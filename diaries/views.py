from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from diaries.models import Diary
from diaries.serializers import DiarySerializers


class DiariesListAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = DiarySerializers

    def get_queryset(self):
        return Diary.objects.all()

