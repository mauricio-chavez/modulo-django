"""Movies app models"""

from django.db import models


class Movie(models.Model):
    """Movie model"""
    name = models.CharField('nombre', max_length=255)
    director = models.CharField('director', max_length=255)
    release_date = models.DateField('fecha de lanzamiento')
    created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
    updated_at = models.DateTimeField('última actualización', auto_now=True)

    def __str__(self):
        """Returns a string representation of a movie"""
        return self.name

    class Meta:
        """Meta attributes of a movie"""
        verbose_name = 'película'
