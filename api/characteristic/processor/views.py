from characteristics.models import ProcessorType, OperationSystem
from .serializers import ProcessorTypeSerializer, OperationSystemSerializer
from api.characteristic.mixins import BaseClassView


class ProcessorTypeView(BaseClassView):
    def get(self, request, **kwargs):
        return super().get(
            request,
            pk=kwargs.get("pk"),
            model=ProcessorType,
            serializer=ProcessorTypeSerializer,
        )

    def post(self, request, *args, **kwargs):
        return super().post(
            request,
            serializer=ProcessorTypeSerializer,
        )

    def put(self, request, *args, **kwargs):
        return super().put(
            request,
            model=ProcessorType,
            pk=kwargs.get("pk"),
            serializer=ProcessorTypeSerializer,
        )

    def delete(self, request, *args, **kwargs):
        return super().delete(request, model=ProcessorType, pk=kwargs.get("pk"))


class OperationSystemView(BaseClassView):
    def get(self, request, **kwargs):
        return super().get(
            request,
            pk=kwargs.get("pk"),
            model=OperationSystem,
            serializer=OperationSystemSerializer,
        )

    def post(self, request, *args, **kwargs):
        return super().post(
            request,
            serializer=OperationSystemSerializer,
        )

    def put(self, request, *args, **kwargs):
        return super().put(
            request,
            model=OperationSystem,
            pk=kwargs.get("pk"),
            serializer=OperationSystemSerializer,
        )

    def delete(self, request, *args, **kwargs):
        return super().delete(request, model=OperationSystem, pk=kwargs.get("pk"))
