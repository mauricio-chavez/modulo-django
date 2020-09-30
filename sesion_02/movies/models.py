from django.db import models


class Director(models.Model):
    """Director model"""
    name = models.CharField(max_length=100)
    birthday = models.DateField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    director = models.ForeignKey(to=Director, on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField()
    sinopsis = models.TextField()

    def __str__(self):
        return self.name + ' de ' + self.director.name
