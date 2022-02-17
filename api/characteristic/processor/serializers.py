from rest_framework.serializers import ModelSerializer

from characteristics.models import ProcessorType, OperationSystem


class ProcessorTypeSerializer(ModelSerializer):
    class Meta:
        model = ProcessorType
        fields = "__all__"


class OperationSystemSerializer(ModelSerializer):
    class Meta:
        model = OperationSystem
        fields = "__all__"
