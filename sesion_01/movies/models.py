from django.db import models


class Item(models.Model):
    """Item"""
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
