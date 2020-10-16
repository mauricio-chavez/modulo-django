"""Movies app admin site"""

from django.contrib import admin

from .models import Movie

admin.site.register(Movie)
