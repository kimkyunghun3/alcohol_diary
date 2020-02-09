from django.shortcuts import render
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_framework import generics, permissions

from users.serializers import UserSerializers
from users.models import User

#
# class KakaoLogin(SocialLoginView):
#     adapter_class = KakaoOAuth2Adapter


# def social_login(request):
#     token = request.GET["code"]


class UserListAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializers

    def get_queryset(self):
        return User.objects.all()


class UserOnlyAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializers

    def get_queryset(self):
        return User.objects.all()
