from rest_framework.serializers import ModelSerializer
from characteristics.models import ProductType
from rest_framework.serializers import (
    ModelSerializer,
)


class ProductTypeSerializer(ModelSerializer):
    class Meta:
        model = ProductType
        fields = "__all__"
