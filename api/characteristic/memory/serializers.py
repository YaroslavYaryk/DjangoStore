from rest_framework.serializers import ModelSerializer

from characteristics.models import (
    MemoryCapacity,
    MemorySlot,
    MemoryType,
    DataStorageDevices,
)


class MemoryCapacitySerializer(ModelSerializer):
    class Meta:
        model = MemoryCapacity
        fields = "__all__"


class MemorySlotSerializer(ModelSerializer):
    class Meta:
        model = MemorySlot
        fields = "__all__"


class MemoryTypeSerializer(ModelSerializer):
    class Meta:
        model = MemoryType
        fields = "__all__"


class DataStorageDevicesSerializer(ModelSerializer):
    class Meta:
        model = DataStorageDevices
        fields = "__all__"
