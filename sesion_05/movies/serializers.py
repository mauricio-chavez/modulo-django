"""Movies app serializers"""

from rest_framework import serializers

from .models import Movie, Director


class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes directors"""
    url = serializers.HyperlinkedIdentityField(
        view_name="movies:director-detail"
    )

    class Meta:
        model = Director
        fields = ['url', 'first_name', 'last_name', 'birthday']


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes movies"""
    url = serializers.HyperlinkedIdentityField(view_name="movies:movie-detail")
    director = serializers.HyperlinkedRelatedField(
        view_name='movies:director-detail',
        read_only=True
    )

    class Meta:
        model = Movie
        fields = ['url', 'name', 'director', 'release_date']

    # id = serializers.IntegerField(required=False)
    # name = serializers.CharField()
    # director_id = serializers.IntegerField()
    # release_date = serializers.DateField()

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Movie` instance, given the validated data.
    #     """
    #     return Movie.objects.create(**validated_data)

    # def update(self, movie, validated_data):
    #     """
    #      Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     name = validated_data.get('name')
    #     director_id = validated_data.get('director_id')
    #     release_date = validated_data.get('release_date')

    #     movie.name = name if name else movie.name
    #     movie.director_id = director_id if director_id else movie.director_id
    #     movie.release_date = release_date if release_date else movie.release_date

    #     movie.save()
    #     return movie
