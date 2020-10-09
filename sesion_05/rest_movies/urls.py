"""Project URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include(('movies.urls', 'movies'), namespace='movies')),
    path('api-auth/', include('rest_framework.urls'))
]
