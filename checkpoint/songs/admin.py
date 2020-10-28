"""Songs app admin"""

from django.contrib import admin

from .models import Album


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    """Admin View for Album"""
    list_display = ['name', 'cover']
    list_filter = ['name', ]
    search_fields = ['name', ]
    ordering = ['name', ]
