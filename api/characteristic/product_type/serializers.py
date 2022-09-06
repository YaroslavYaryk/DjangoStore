from rest_framework.serializers import ModelSerializer
from characteristics.models import ProductType
from rest_framework.serializers import (
    ModelSerializer,
)
from rest_framework.fields import SerializerMethodField
from decouple import config


class ProductTypeSerializer(ModelSerializer):

    icon = SerializerMethodField()
    photo = SerializerMethodField()

    class Meta:
        model = ProductType
        fields = "__all__"

    def get_icon(self, instance):
        return f"{config('USERHOST')}:{config('USERPORT')}{instance.icon.url}"

    def get_photo(self, instance):
        return f"{config('USERHOST')}:{config('USERPORT')}{instance.photo.url}"
