"""Songs app models"""

from django.db import models

from core.models import TimestampModel


class Track(TimestampModel):
    """Track model"""
    name = models.CharField('nombre', max_length=255)
    artist = models.ForeignKey(
        verbose_name='artista',
        to='Artist',
        on_delete=models.CASCADE
    )
    album = models.ForeignKey(
        verbose_name='album',
        to='Album',
        on_delete=models.CASCADE
    )

    def __str__(self):
        """Returns a string representation of track"""
        return self.name

    class Meta:
        verbose_name = 'canción'
        verbose_name_plural = 'canciones'



class Artist(TimestampModel):
    """Artist model"""
    name = models.CharField('nombre', max_length=255)
    birthday = models.DateField('cumpleaños')

    def __str__(self):
        """Returns a string representation of artist"""
        return self.name

    class Meta:
        verbose_name = 'artista'


class Album(TimestampModel):
    """Album model"""
    name = models.CharField('nombre', max_length=255)
    release_year = models.PositiveSmallIntegerField('año de lanzamiento')

    def __str__(self):
        """Returns a string representation of album"""
        return self.name
