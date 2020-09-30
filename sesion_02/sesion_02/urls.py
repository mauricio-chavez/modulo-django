"""sesion_02 URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include(('movies.urls', 'movies'), namespace='movies')),
    path('', include(('users.urls', 'users'), namespace='users')),
]
