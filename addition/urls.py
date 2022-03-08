''' defines path to addition of two numbers'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.AdditionAPIView.as_view(), name='AdditionAPIView'),
]