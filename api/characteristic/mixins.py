from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.utils.text import slugify


class BaseClassView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            queryset = kwargs["model"].objects.get(pk=kwargs["pk"])
            serializer = kwargs["serializer"](queryset)
        else:
            queryset = kwargs["model"].objects.all()
            serializer = kwargs["serializer"](queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = kwargs["serializer"](data=request.data)
        if serializer.is_valid():
            if not serializer.validated_data.get(
                "slug"
            ) and serializer.validated_data.get("name"):
                serializer.validated_data["slug"] = slugify(
                    serializer.validated_data.get("name")
                )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        post = kwargs["model"].objects.get(pk=kwargs["pk"])
        serializer = kwargs["serializer"](instance=post, data=request.data)
        if serializer.is_valid():
            if not serializer.validated_data.get(
                "slug"
            ) and serializer.validated_data.get("name"):
                serializer.validated_data["slug"] = slugify(
                    serializer.validated_data.get("name")
                )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        post = kwargs["model"].objects.get(pk=kwargs["pk"])
        post.delete()
        return Response({"message": "Item was succesfully deleted"})
