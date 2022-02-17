from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.utils.text import slugify

from characteristics.models import ProductType
from .serializers import ProductTypeSerializer


class ProductTypeView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        if kwargs:
            queryset = ProductType.objects.get(pk=kwargs["pk"])
            serializer = ProductTypeSerializer(queryset)
        else:
            queryset = ProductType.objects.all()
            serializer = ProductTypeSerializer(queryset, many=True)
            print(queryset)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductTypeSerializer(data=request.data)
        if serializer.is_valid():

            if not serializer.validated_data.get("slug"):
                serializer.validated_data["slug"] = slugify(
                    serializer.validated_data.get("name")
                )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        post = ProductType.objects.get(pk=pk)
        serializer = ProductTypeSerializer(instance=post, data=request.data)
        print(post.name)

        if serializer.is_valid():

            if not serializer.validated_data.get("slug"):
                if serializer.validated_data.get("name"):
                    serializer.validated_data["slug"] = slugify(
                        serializer.validated_data.get("name")
                    )
                else:
                    serializer.validated_data["slug"] = slugify(post.name)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requset, pk):
        post = ProductType.objects.get(pk=pk)
        post.delete()
        return Response({"message": "Item was succesfully deleted"})
