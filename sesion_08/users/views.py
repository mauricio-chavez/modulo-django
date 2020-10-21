"""Users app views"""

from django.contrib.auth import get_user_model

from rest_framework import viewsets

from .serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """User viewset"""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
