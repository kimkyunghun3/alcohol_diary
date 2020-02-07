from django.shortcuts import render
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter


def social_login(request):
    token = request.GET["code"]
