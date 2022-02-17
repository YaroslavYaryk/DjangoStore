from rest_framework.serializers import ModelSerializer


from characteristics.models import (
    ScreenDiagonal,
    ScreenType,
    ScreenFrequency,
)


class ScreenDiagonalSerializer(ModelSerializer):
    class Meta:
        model = ScreenDiagonal
        fields = "__all__"


class ScreenTypeSerializer(ModelSerializer):
    class Meta:
        model = ScreenType
        fields = "__all__"


class ScreenFrequencySerializer(ModelSerializer):
    class Meta:
        model = ScreenFrequency
        fields = "__all__"
