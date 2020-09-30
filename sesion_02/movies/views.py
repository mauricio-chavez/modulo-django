from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Movie, Director


@login_required
def list_movies(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/list.html', context)


@login_required
def create(request):
    context = {}

    if request.method == 'POST':
        name = request.POST.get('name')
        year = request.POST.get('year')
        year = int(year)
        sinopsis = request.POST.get('sinopsis')
        tarantino = Director.objects.get(id=1)

        movie = Movie.objects.create(
            name=name,
            year=year,
            sinopsis=sinopsis,
            director=tarantino
        )

        context['movie'] = movie

    return render(request, 'movies/create.html', context)
