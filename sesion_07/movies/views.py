"""Movies app views"""

from django.views.generic import ListView

from .models import Movie


class MovieListView(ListView):
    """Lists all movies"""
    model = Movie
    template_name = 'movies/list.html'
