from rest_framework import serializers
from users.models import NewUser
from django.contrib.auth import get_user_model
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """

    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = NewUser
        fields = ("email", "user_name", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class CreateUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    class Meta:
        model = get_user_model()
        fields = ("email", "password", "username", "first_name", "last_name")
        write_only_fields = "password"
        read_only_fields = (
            "is_staff",
            "is_superuser",
            "is_active",
        )

    def create(self, validated_data):
        user = super(CreateUserSerializer, self).create(validated_data)
        user.set_password(validated_data["password"])
        print(user.password)

        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    class Meta:
        model = get_user_model()
        fields = "__all__"
        write_only_fields = "password"


class UserEditBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("email", "first_name", "last_name", "middle_name", "phone")


class UserLivingPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "living_place")


class UserWareHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "ware_house")


class UserDeliveryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "delivery_type")
