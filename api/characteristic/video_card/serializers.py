from rest_framework.serializers import ModelSerializer

from characteristics.models import VideoCard, VideoCardMemory


class VideoCardSerializer(ModelSerializer):
    class Meta:
        model = VideoCard
        fields = "__all__"


class VideoCardMemorySerializer(ModelSerializer):
    class Meta:
        model = VideoCardMemory
        fields = "__all__"
