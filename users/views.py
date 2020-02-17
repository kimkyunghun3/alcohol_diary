from rest_framework import generics, permissions
from users.serializers import UserSerializers, UserCreateSerializer
from users.models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView


class UserListAPI(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializers

    def get_queryset(self):
        return User.objects.all()


class KakaoBackend:
    def authenticate(self, request, kakao_id):
        try:
            user = User.objects.get(username=kakao_id)
        except User.DoesNotExist:
            user = User(username=kakao_id)
            user.save()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class AuthTokenAPIView(APIView):
    def post(self, request):

        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
        else:
            raise AuthenticationFailed()

        data = {
            'token': token.key,
        }
        return Response(data)


class SnippetListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    def get_serializer_class(self):

        if self.request.method == 'GET':
            return UserSerializers
        elif self.request.method == 'POST':
            return UserCreateSerializer

    def perform_create(self, serializer):

        serializer.save(author=self.request.user)

