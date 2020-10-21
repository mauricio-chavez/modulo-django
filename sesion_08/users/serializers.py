"""Users app serializers"""

from rest_framework import serializers

from django.contrib.auth import get_user_model


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """User serializer"""
    url = serializers.HyperlinkedIdentityField(view_name='users:user-detail')

    class Meta:
        model = get_user_model()
        fields = ['url', 'username', 'email', 'first_name', 'last_name']
