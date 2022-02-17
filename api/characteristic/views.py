from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from store.models import Characteristics, ProductImage

from .serializers import (
    ProductCharacteristicSerializer,
    ProductCharacteristicPostSerializer,
    ProductImagesSerializer,
)


class ProductCharacteristicView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, product_id):

        queryset = Characteristics.objects.get(product__pk=product_id)
        serializer = ProductCharacteristicSerializer(queryset)

        return Response(serializer.data)

    def post(self, request):
        serializer = ProductCharacteristicPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, product_id):
        post = Characteristics.objects.get(product__pk=product_id)
        serializer = ProductCharacteristicPostSerializer(
            instance=post, data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductImageView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):

        queryset = ProductImage.objects.filter(product__pk=pk)
        serializer = ProductImagesSerializer(queryset, many=True)

        return Response(serializer.data)
