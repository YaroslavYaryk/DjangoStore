from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.utils.text import slugify

from characteristics.models import CountryBrand, CountryMade
from .serializers import CountryBrandSerializer, CountryMadeSerializer


class CountryBrandView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        if kwargs:
            queryset = CountryBrand.objects.get(pk=kwargs["pk"])
            serializer = CountryBrandSerializer(queryset)
        else:
            queryset = CountryBrand.objects.all()
            serializer = CountryBrandSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CountryBrandSerializer(data=request.data)
        if serializer.is_valid():
            if not serializer.validated_data.get("slug"):
                serializer.validated_data["slug"] = slugify(
                    serializer.validated_data.get("name")
                )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        post = CountryBrand.objects.get(pk=pk)
        serializer = CountryBrandSerializer(instance=post, data=request.data)

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
        post = CountryBrand.objects.get(pk=pk)
        post.delete()
        return Response({"message": "Item was succesfully deleted"})


class CountryMadeView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        if kwargs:
            queryset = CountryMade.objects.get(pk=kwargs["pk"])
            serializer = CountryMadeSerializer(queryset)
        else:
            queryset = CountryMade.objects.all()
            serializer = CountryMadeSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CountryMadeSerializer(data=request.data)
        if serializer.is_valid():
            if not serializer.validated_data.get("slug"):
                serializer.validated_data["slug"] = slugify(
                    serializer.validated_data.get("name")
                )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        post = CountryMade.objects.get(pk=pk)
        serializer = CountryMadeSerializer(instance=post, data=request.data)

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
        post = CountryMade.objects.get(pk=pk)
        post.delete()
        return Response({"message": "Item was succesfully deleted"})
