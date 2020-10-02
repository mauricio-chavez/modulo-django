"""Canciones app models"""

from django.db import models


class TimestampModel(models.Model):
    """Model with timestamps"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Album(TimestampModel):
    """Album model"""
    name = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='albums')

    def __str__(self):
        return self.name


class Artist(TimestampModel):
    """Artist model"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Song(TimestampModel):
    """Song model"""
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(to='Artist', on_delete=models.CASCADE)
    album = models.ForeignKey(to='Album', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
