"""Songs app admin"""

from django.contrib import admin

from .models import Track, Artist, Album

admin.site.register(Track)
admin.site.register(Artist)
admin.site.register(Album)
