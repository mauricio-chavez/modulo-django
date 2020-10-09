"""Movies app views"""

# Standard Library

# Django
from django.http import JsonResponse
from django.views.generic import View

# Third Party
from rest_framework import viewsets, status
from rest_framework.response import Response


# Locals
from .models import Movie, Director
from .serializers import MovieSerializer, DirectorSerializer


class MoviesViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class DirectorViewset(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


# class MoviesViewset(viewsets.ViewSet):
#     """Movies viewsets"""

#     def list(self, request):
#         """Shows all movies"""
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk):
#         """Retrieves a movies"""
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = MovieSerializer(request.data)
#         movie = Movie.objects.create(**serializer.data)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def delete(self, request, pk):
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie)
#         movie.delete()
#         return Response(serializer.data)


# class HelloWorldView(View):
#     """Greets a user"""

#     def get(self, request):
#         """Greets a user in GET method"""
#         data = {
#             'success': True,
#             'data': 'Hola, mundo'
#         }
#         return JsonResponse(data)
