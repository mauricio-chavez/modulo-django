"""Products app models"""

from django.contrib.auth import get_user_model
from django.db import models


class ProductManager(models.Manager):
    """Product base manager"""

    def create_regular_product(self, name, price, user):
        """Creates a regular product"""
        return self.create(name=name, price=price, user=user, rating=3)


class Product(models.Model):
    """Product model"""
    name = models.CharField('producto', max_length=100)
    price = models.DecimalField('precio', max_digits=9, decimal_places=2)
    WORST = 1
    BAD = 2
    REGULAR = 3
    GOOD = 4
    BEST = 5
    RATING_CHOICES = (
        (WORST, 'Pésimo'),
        (BAD, 'Malo'),
        (REGULAR, 'Regular'),
        (GOOD, 'Bueno'),
        (BEST, 'Excelente'),
    )
    rating = models.PositiveSmallIntegerField(
        'calificación', choices=RATING_CHOICES
    )
    user = models.ForeignKey(
        verbose_name='usuario',
        to=get_user_model(),
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField('fecha de creación', auto_now_add=True)
    updated_at = models.DateTimeField('fecha de actualización', auto_now=True)
    objects = ProductManager()

    def __str__(self):
        """Return a product string representation"""
        return f'{self.name} - ${self.price}'
