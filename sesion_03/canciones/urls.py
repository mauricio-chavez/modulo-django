"""Canciones app URL config"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_songs, name='list'),
]
