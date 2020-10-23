"""Users app views"""

from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import UserSerializer, LocationSerializer
from .models import Location


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """User viewset"""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LocationViewSet(viewsets.ModelViewSet):
    """Location viewset"""
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
