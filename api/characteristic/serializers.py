from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (
    ModelSerializer,
)

from .screen.serializers import (
    ScreenDiagonalSerializer,
    ScreenFrequencySerializer,
    ScreenTypeSerializer,
)
from .processor.serializers import OperationSystemSerializer, ProcessorTypeSerializer
from .memory.serializers import (
    DataStorageDevicesSerializer,
    MemoryCapacitySerializer,
    MemorySlotSerializer,
    MemoryTypeSerializer,
)
from .video_card.serializers import VideoCardMemorySerializer, VideoCardSerializer
from store.models import Characteristics, ProductImage


class ProductCharacteristicSerializer(ModelSerializer):

    diagonal_screen = ScreenDiagonalSerializer()
    screen_type = ScreenTypeSerializer()
    screen_frequency = ScreenFrequencySerializer()
    processor_name = ProcessorTypeSerializer()
    operation_system = OperationSystemSerializer()
    memory_capacity = MemoryCapacitySerializer()
    memory_slots = MemorySlotSerializer()
    memory_type = MemoryTypeSerializer()
    data_storage = DataStorageDevicesSerializer()
    video_card = VideoCardSerializer()
    video_card_memory = VideoCardMemorySerializer()

    class Meta:
        model = Characteristics
        exclude = ("product",)


class ProductCharacteristicPostSerializer(ModelSerializer):
    class Meta:
        model = Characteristics
        fields = "__all__"


class ProductImagesSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            "id",
            "images",
        )


class ProductVideoSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            "id",
            "images",
        )
