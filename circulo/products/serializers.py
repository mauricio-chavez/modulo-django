"""Products app serializers"""

from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """Product hyperlinked serializer"""
    url = serializers.HyperlinkedIdentityField(
        view_name='products:product-detail'
    )
    user = serializers.HyperlinkedRelatedField(
        view_name='users:user-detail',
        read_only=True
    )

    class Meta:
        model = Product
        fields = [
            'url', 'name', 'price', 'rating', 'user', 'created_at', 'updated_at'
        ]
