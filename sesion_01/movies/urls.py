"""Movies URL's"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello_world),
    path('suma/', views.suma)
]
