from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination

from diaries.filters import DiaryFilter
from diaries.models import Diary
from diaries.serializers import DiarySerializers


class DiariesListCreateAPI(generics.ListCreateAPIView):
    # 페이지 관련 세팅 변경 시
    # https://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = DiarySerializers
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = DiaryFilter

    def get_queryset(self):
        return Diary.objects.all()


class DiariesRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = DiarySerializers

    def get_queryset(self):
        return Diary.objects.all()

