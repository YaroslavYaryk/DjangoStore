from rest_framework.serializers import ModelSerializer
from characteristics.models import CountryBrand, CountryMade
from rest_framework.serializers import (
    ModelSerializer,
)


class CountryBrandSerializer(ModelSerializer):
    class Meta:
        model = CountryBrand
        fields = "__all__"


class CountryMadeSerializer(ModelSerializer):
    class Meta:
        model = CountryMade
        fields = "__all__"
