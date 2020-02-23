from django.urls import path
from . import views

app_name = 'diaries'

urlpatterns = [
    path('<int:pk>/', views.DiariesRetrieveAPIView.as_view()),
    path('', views.DiariesListCreateAPI.as_view(), name='Diary'),
]
