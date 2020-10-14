"""Proyect schema"""

import graphene

from songs.schema import Query as SongsQuery, Mutation as SongsMutation


class Query(SongsQuery, graphene.ObjectType):
    """Root Query

    type Query {
        hello: String!
    }
    """
    hello = graphene.String(required=True)

    def resolve_hello(*args, **kwargs):
        """greets a user"""
        return 'Hello from a resolver!'


class Mutation(SongsMutation, graphene.ObjectType):
    """Root Mutation"""


schema = graphene.Schema(query=Query, mutation=Mutation)
