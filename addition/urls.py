''' defines path to addition of two numbers'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdditionDetail.as_view(), name='AdditionDetail'),
    path('<int:pk>', views.AdditionDetail.as_view(), name='AdditionDetail'),

]

