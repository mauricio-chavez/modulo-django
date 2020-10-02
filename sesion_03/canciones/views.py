"""Canciones app views"""

from django.shortcuts import render

from .models import Song


def list_songs(request):
    """Lists all songs"""
    songs = Song.objects.all().prefetch_related()
    return render(request, 'songs/list.html', {'songs': songs})
