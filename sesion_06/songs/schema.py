"""Songs app GraphQL schema"""

from django.shortcuts import get_object_or_404

import graphene
from graphene_django import DjangoObjectType

from .models import Track, Artist, Album

# Types (objetos)


class TrackType(DjangoObjectType):
    """Track type for schema

    type Track {
        name: String!
        artist: Artist!
        album: Album!
    }
    """
    class Meta:
        model = Track
        fields = ('id', 'name', 'artist', 'album')


class ArtistType(DjangoObjectType):
    """Track type for schema

    type Artist {
        name: String!
        birthday: String!
    }
    """
    class Meta:
        model = Artist
        fields = ('id', 'name', 'birthday')


class AlbumType(DjangoObjectType):
    """Track type for schema

    type Album {
        name: String!
        release_year: Int!
    }
    """
    class Meta:
        model = Album
        fields = ('id', 'name', 'release_year')


# Mutation

class AlbumMutation(graphene.Mutation):
    """Creates a new album"""
    class Arguments:
        """Mutation argument"""
        name = graphene.String(required=True)
        release_year = graphene.Int(required=True)

    album = graphene.Field(AlbumType)

    def mutate(self, info, name, release_year):
        """Creates album and returns it"""
        album = Album.objects.create(name=name, release_year=release_year)
        return AlbumMutation(album=album)


# Root Objects

class Query:
    """Micro Query type for songs app schema

    type Query {
        allTracks: [Song!]!
        getTrack(id: Int!): Song!
    }
    """
    all_tracks = graphene.List(TrackType, required=True)
    get_track = graphene.Field(TrackType, id=graphene.Int(required=True))
    all_albums = graphene.List(AlbumType, required=True)

    def resolve_all_tracks(root, info):
        """Returns all tracks"""
        # import pdb; pdb.set_trace()
        # breakpoint() for Python 3.7+
        return Track.objects.select_related('artist', 'album').all()

    def resolve_get_track(root, info, id):
        """Returns a track"""
        return get_object_or_404(Track, id=id)

    def resolve_all_albums(root, info):
        """Returns all albums"""
        return Album.objects.all()


class Mutation:
    """Micro Mutation type for songs app schema

    type Mutation {
        createAlbum(name: String, releaseYear: Int): Album!
    }
    """
    create_album = AlbumMutation.Field(required=True)
