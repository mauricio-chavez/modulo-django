"""Project URL Configuration"""

from django.urls import path, include

urlpatterns = [
    path('', include(('users.urls', 'users'), namespace='users')),
]
