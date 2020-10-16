"""Movies app URL config"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.MovieListView.as_view(), name='list'),
]
