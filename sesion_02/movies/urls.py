from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_movies, name='list'),
    path('create/', views.create, name='create'),
]
