"""Defines url patterns for vue_list_example app"""
from django.urls import path
from . import views

app_name = 'vue_list_example'
urlpatterns = [
    #Home Page
    path('', views.index, name='index'),
]