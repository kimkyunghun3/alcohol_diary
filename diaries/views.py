from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination

from diaries.filters import DiaryFilter
from diaries.models import Diary
from diaries.serializers import DiarySerializers, DiaryCreateSerializers


class DiariesListCreateAPI(generics.ListCreateAPIView):
    # 페이지 관련 세팅 변경 시
    # https://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination
    # permission_classes = [permissions.IsAuthenticated, ]
    serializer_classes = {
        'GET': DiarySerializers,
        'POST': DiaryCreateSerializers,
    }
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = DiaryFilter

    def get_serializer_class(self):
        return self.serializer_classes[self.request.method]

    def get_queryset(self):
        return Diary.objects.order_by('-pk')


class DiariesRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = DiarySerializers

    def get_queryset(self):
        return Diary.objects.all()
