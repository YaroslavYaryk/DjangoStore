from characteristics.models import VideoCard, VideoCardMemory
from .serializers import VideoCardSerializer, VideoCardMemorySerializer
from api.characteristic.mixins import BaseClassView


class VideoCardView(BaseClassView):
    def get(self, request, **kwargs):
        return super().get(
            request,
            pk=kwargs.get("pk"),
            model=VideoCard,
            serializer=VideoCardSerializer,
        )

    def post(self, request, *args, **kwargs):
        return super().post(
            request,
            serializer=VideoCardSerializer,
        )

    def put(self, request, *args, **kwargs):
        return super().put(
            request,
            model=VideoCard,
            pk=kwargs.get("pk"),
            serializer=VideoCardSerializer,
        )

    def delete(self, request, *args, **kwargs):
        return super().delete(request, model=VideoCard, pk=kwargs.get("pk"))


class VideoCardMemoryView(BaseClassView):
    def get(self, request, **kwargs):
        return super().get(
            request,
            pk=kwargs.get("pk"),
            model=VideoCardMemory,
            serializer=VideoCardMemorySerializer,
        )

    def post(self, request, *args, **kwargs):
        return super().post(
            request,
            serializer=VideoCardMemorySerializer,
        )

    def put(self, request, *args, **kwargs):
        return super().put(
            request,
            model=VideoCardMemory,
            pk=kwargs.get("pk"),
            serializer=VideoCardMemorySerializer,
        )

    def delete(self, request, *args, **kwargs):
        return super().delete(request, model=VideoCardMemory, pk=kwargs.get("pk"))
