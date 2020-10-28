"""Songs app serializers"""

from rest_framework import serializers

from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    """Album serializer"""
    class Meta:
        model = Album
        fields = '__all__'
