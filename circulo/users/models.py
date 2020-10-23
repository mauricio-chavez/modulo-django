"""Users app models"""

from django.db import models
from django.core.serializers.json import DjangoJSONEncoder


class Location(models.Model):
    """Gets users location"""
    json = models.JSONField(
        encoder=DjangoJSONEncoder,
        db_column='json'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users_location'
        managed = False
