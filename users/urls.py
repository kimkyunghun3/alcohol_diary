from django.conf.urls import include, url

from . import views
# from .views import KakaoLogin

app_name = 'users'

urlpatterns = [
    # url('rest-auth/kakao', KakaoLogin.as_view(), name='kakao_login'),
    # url('users/kakao/login/callback', views.social_login),
    url('', views.UserListAPI.as_view(), name='UserIP'),
    url('<uuid:pk>/', views.UserOnlyAPI.as_view(), name='UserOnly'),
]
