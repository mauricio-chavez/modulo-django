"""Songs app models"""

from django.db import models


class Album(models.Model):
    """Album model"""
    name = models.CharField('nombre', max_length=150)
    cover = models.ImageField('portada', upload_to='covers')

    def __str__(self):
        """Returns an album string representation"""
        return self.name
