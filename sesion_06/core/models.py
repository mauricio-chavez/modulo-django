"""Core app models"""

from django.db import models


class TimestampModel(models.Model):
    """Adds timestamps to models"""
    created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
    updated_at = models.DateTimeField('última actualización', auto_now=True)

    class Meta:
        abstract = True
