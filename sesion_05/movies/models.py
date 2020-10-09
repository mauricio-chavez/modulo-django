"""Movies app models"""

from django.db import models


class Director(models.Model):
    """Movie director model"""
    first_name = models.CharField('nombre(s)', max_length=100)
    last_name = models.CharField('apellido(s)', max_length=100)
    birthday = models.DateField('cumpleaños')
    created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
    updated_at = models.DateTimeField('última actualización', auto_now=True)

    def __str__(self):
        """Returns director string representation"""
        return self.first_name + ' ' + self.last_name


class Movie(models.Model):
    """Movie model"""
    name = models.CharField('nombre', max_length=100)
    director = models.ForeignKey(to='Director', on_delete=models.CASCADE)
    release_date = models.DateField('fecha de salida')
    created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
    updated_at = models.DateTimeField('última actualización', auto_now=True)

    def __str__(self):
        """Returns a movie string representation"""
        return self.name
