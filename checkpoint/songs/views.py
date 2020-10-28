"""Songs app views"""

from rest_framework import viewsets

from .models import Album
from .serializers import AlbumSerializer


class AlbumViewset(viewsets.ModelViewSet):
    """Album viewset"""
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
