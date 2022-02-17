from characteristics.models import (
    ScreenDiagonal,
    ScreenType,
    ScreenFrequency,
)
from .serializers import (
    ScreenDiagonalSerializer,
    ScreenTypeSerializer,
    ScreenFrequencySerializer,
)
from api.characteristic.mixins import BaseClassView


class ScreenDiagonalView(BaseClassView):
    def get(self, request, **kwargs):
        return super().get(
            request,
            pk=kwargs.get("pk"),
            model=ScreenDiagonal,
            serializer=ScreenDiagonalSerializer,
        )

    def post(self, request, *args, **kwargs):
        return super().post(
            request,
            serializer=ScreenDiagonalSerializer,
        )

    def put(self, request, *args, **kwargs):
        return super().put(
            request,
            model=ScreenDiagonal,
            pk=kwargs.get("pk"),
            serializer=ScreenDiagonalSerializer,
        )

    def delete(self, request, *args, **kwargs):
        return super().delete(request, model=ScreenDiagonal, pk=kwargs.get("pk"))


class ScreenTypeView(BaseClassView):
    def get(self, request, **kwargs):
        return super().get(
            request,
            pk=kwargs.get("pk"),
            model=ScreenType,
            serializer=ScreenTypeSerializer,
        )

    def post(self, request, *args, **kwargs):
        return super().post(
            request,
            serializer=ScreenTypeSerializer,
        )

    def put(self, request, *args, **kwargs):
        return super().put(
            request,
            model=ScreenType,
            pk=kwargs.get("pk"),
            serializer=ScreenTypeSerializer,
        )

    def delete(self, request, *args, **kwargs):
        return super().delete(request, model=ScreenType, pk=kwargs.get("pk"))


class ScreenFrequencyView(BaseClassView):
    def get(self, request, **kwargs):
        return super().get(
            request,
            pk=kwargs.get("pk"),
            model=ScreenFrequency,
            serializer=ScreenFrequencySerializer,
        )

    def post(self, request, *args, **kwargs):
        return super().post(
            request,
            serializer=ScreenFrequencySerializer,
        )

    def put(self, request, *args, **kwargs):
        return super().put(
            request,
            model=ScreenFrequency,
            pk=kwargs.get("pk"),
            serializer=ScreenFrequencySerializer,
        )

    def delete(self, request, *args, **kwargs):
        return super().delete(request, model=ScreenFrequency, pk=kwargs.get("pk"))
