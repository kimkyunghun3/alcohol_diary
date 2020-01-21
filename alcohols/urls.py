from django.urls import path
from . import views

app_name = 'alcohols'

urlpatterns = [
    path('', views.AlcoholRecordListAPI.as_view(), name='AlcoholRecord'),
]
