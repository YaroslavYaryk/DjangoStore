from characteristics.models import (
    MemoryCapacity,
    MemorySlot,
    MemoryType,
    DataStorageDevices,
)
from .serializers import (
    MemoryCapacitySerializer,
    DataStorageDevicesSerializer,
    MemorySlotSerializer,
    MemoryTypeSerializer,
)
from api.characteristic.mixins import BaseClassView


class MemoryCapacityView(BaseClassView):
    def get(self, request, **kwargs):
        return super().get(
            request,
            pk=kwargs.get("pk"),
            model=MemoryCapacity,
            serializer=MemoryCapacitySerializer,
        )

    def post(self, request, *args, **kwargs):
        return super().post(
            request,
            serializer=MemoryCapacitySerializer,
        )

    def put(self, request, *args, **kwargs):
        return super().put(
            request,
            model=MemoryCapacity,
            pk=kwargs.get("pk"),
            serializer=MemoryCapacitySerializer,
        )

    def delete(self, request, *args, **kwargs):
        return super().delete(request, model=MemoryCapacity, pk=kwargs.get("pk"))


class MemorySlotView(BaseClassView):
    def get(self, request, **kwargs):
        return super().get(
            request,
            pk=kwargs.get("pk"),
            model=MemorySlot,
            serializer=MemorySlotSerializer,
        )

    def post(self, request, *args, **kwargs):
        return super().post(
            request,
            serializer=MemorySlotSerializer,
        )

    def put(self, request, *args, **kwargs):
        return super().put(
            request,
            model=MemorySlot,
            pk=kwargs.get("pk"),
            serializer=MemorySlotSerializer,
        )

    def delete(self, request, *args, **kwargs):
        return super().delete(request, model=MemorySlot, pk=kwargs.get("pk"))


class MemoryTypeView(BaseClassView):
    def get(self, request, **kwargs):
        return super().get(
            request,
            pk=kwargs.get("pk"),
            model=MemoryType,
            serializer=MemoryTypeSerializer,
        )

    def post(self, request, *args, **kwargs):
        return super().post(
            request,
            serializer=MemoryTypeSerializer,
        )

    def put(self, request, *args, **kwargs):
        return super().put(
            request,
            model=MemoryType,
            pk=kwargs.get("pk"),
            serializer=MemoryTypeSerializer,
        )

    def delete(self, request, *args, **kwargs):
        return super().delete(request, model=MemoryType, pk=kwargs.get("pk"))


class DataStorageDevicesView(BaseClassView):
    def get(self, request, **kwargs):
        return super().get(
            request,
            pk=kwargs.get("pk"),
            model=DataStorageDevices,
            serializer=DataStorageDevicesSerializer,
        )

    def post(self, request, *args, **kwargs):
        return super().post(
            request,
            serializer=DataStorageDevicesSerializer,
        )

    def put(self, request, *args, **kwargs):
        return super().put(
            request,
            model=DataStorageDevices,
            pk=kwargs.get("pk"),
            serializer=DataStorageDevicesSerializer,
        )

    def delete(self, request, *args, **kwargs):
        return super().delete(request, model=DataStorageDevices, pk=kwargs.get("pk"))
