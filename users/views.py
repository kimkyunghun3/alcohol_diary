import json

import requests
from rest_framework import generics, permissions
from users.serializers import UserSerializers, UserCreateSerializer
from users.models import User
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView


# class UserListAPI(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticated, ]
#     serializer_class = UserSerializers
#
#     def get_queryset(self):
#         return User.objects.all()


# class KakaoBackend:
#     def authenticate(self, request, kakao_id):
#         try:
#             user = User.objects.get(username=kakao_id)
#         except User.DoesNotExist:
#             user = User(username=kakao_id)
#             user.save()
#         return user
#
#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None
class AuthTokenAPIView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)

        if user is None:
            try:
                user = User.objects.get(username=username)
            except (User.DoesNotExist, User.MultipleObjectsReturned):
                # username 이 없으면 생성
                User.objects.create_user(username=username, password=password)
            else:
                # username 이 있으나 password 가 없는 경우
                if not user.check_password(password):
                    raise ValidationError({'detail': '패스워드가 잘못되었습니다.'})

        token, _ = Token.objects.get_or_create(user=user)
        data = {
            'token': token.key,
        }
        return Response(data)


class KakaoLoginView(APIView):
    def get(self, request):
        kakao_access_code = request.GET.get('code', None)
        kakao_app_key = '8886c592089a4ed719130630690f6b81'

        url = 'https://kauth.kakao.com/oauth/token'
        headers = {'Content-type': 'application/x-www-form-urlencoded; charset=utf-8'}

        body = {'grant_type': 'authorization_code',
                'client_id': kakao_app_key,
                'redirect_url': 'http://localhost:8000/kakao-login',
                'code': kakao_access_code
                }

        token_kakao_response = requests.post(url, headers=headers, data=body)
        access_token = json.loads(token_kakao_response.text).get('access_token')

        url = 'https://kapi.kakao.com/v2/user/me'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-type': 'application/x-www-form-urlencoded; charset=utf-8'
        }

        kakao_response = requests.get(url, headers=headers)
        json_kakao = json.loads(kakao_response.content)

        if json_kakao.get('id'):
            try:
                user = User.objects.get(username=json_kakao.get("id"))
            except(User.DoesNotExist, User.MultipleObjectsReturned):
                user = User.objects.create_user(username=json_kakao.get("id"))
            token, _ = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
            }
            return Response(data)
        else:
            raise ValidationError("로그인은 카카오톡으로만 가능합니다.")


# if username in AuthTokenAPIView:
#     return user.username
#
# else:
#     raise AuthenticationFailed()
# class UserListCreateAPIView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers
#
#     permission_classes = (
#         permissions.IsAuthenticatedOrReadOnly,
#     )
#
#     def get_serializer_class(self):
#
#         if self.request.method == 'GET':
#             return UserSerializers
#         elif self.request.method == 'POST':
#             return UserCreateSerializer
#
#     def perform_create(self, serializer):
#
#         serializer.save(author=self.request.user)
