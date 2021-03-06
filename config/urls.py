"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/alcohols/', include('alcohols.urls', namespace='alcohols')),
                  path('api/v1/diaries/', include('diaries.urls', namespace='diaries')),
                  path('api/v1/usersIP/', include('users.urls', namespace='usersIP')),
                  # path('api/v1/usersOnly', include('users.urls', namespace='usersOnly')),
                  # path('api-jwt-auth/', obtain_jwt_token),
                  # path('api-jwt-auth/refresh/', refresh_jwt_token),
                  # path('api-jwt-auth/verify/', verify_jwt_token),
                  # path('rest-auth/', include('rest_auth.urls')),
                  # path('rest-auth/registration', include('rest_auth.registration.urls')),
                  path('users/', include('users.urls')),
                    path('auth/', include('rest_framework_social_oauth2.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
