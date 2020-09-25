"""Movies views"""

from random import randint

from django.shortcuts import render

from .models import Item


def hello_world(request):
    """Saludando al mundo"""
    random = randint(1, 10)
    items = Item.objects.all()
    context = {
        'number': random,
        'items': items
    }

    return render(request, 'movies/index.html', context)


def suma(request):
    """Toma numeros del parametro suma y regresa el resultado"""
    query = request.GET.get('suma')
    numeros = query.split(',')
    suma = sum(map(int, numeros))
    return HttpResponse('La suma es {}'.format(suma))
