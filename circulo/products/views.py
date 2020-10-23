"""Products app views"""

from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """Viewset for product model"""
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = Product.objects.filter(user=request.user)
        serializer = ProductSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)

        if product.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            product = serializer.validated_data
            product['user'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
