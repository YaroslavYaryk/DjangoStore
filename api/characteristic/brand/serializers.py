from rest_framework.serializers import ModelSerializer
from characteristics.models import ProductBrand
from rest_framework.serializers import (
    ModelSerializer,
)


class BrandSerializer(ModelSerializer):
    class Meta:
        model = ProductBrand
        fields = "__all__"


class ProductTypeSerializer(ModelSerializer):
    class Meta:
        model = ProductBrand
        fields = "__all__"
