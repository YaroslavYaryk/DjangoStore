from rest_framework.serializers import ModelSerializer
from store.models import (
    Product, ProductComment, CommentResponse,
    ProductLike, CartProduct, Cart, LikedComment, Coupon, UserCoupon, UserOrderHistory, UserSearchHistory
)
from django.utils.html import strip_tags
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import (
    ModelSerializer,
)
from api.characteristic.brand.serializers import BrandSerializer, ProductTypeSerializer
from api.characteristic.country_brand_made.serializers import (
    CountryBrandSerializer,
    CountryMadeSerializer,
)


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["description"] = strip_tags(instance.description)
        return data


class ProductPostSerializer(ModelSerializer):
    class Meta:
        model = Product

        fields = (
            "id",
            "name",
            "only_name",
            "slug",
            "description",
            "short_description",
            "photo",
            "video",
            "is_published",
            "warranty",
            "price",
            "brand",
            "type_of_product",
            "country_made",
            "country_brand",
        )

        read_only = ("id",)


class ProductPostPutSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["description"] = strip_tags(instance.description)
        return data


class ProductSerializer(ModelSerializer):

    brand = BrandSerializer()
    type_of_product = ProductTypeSerializer()
    country_made = CountryMadeSerializer()
    country_brand = CountryBrandSerializer()
    photo = SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_photo(self, instance):
        try:
            image = instance.photo.url
        except Exception:
            image = None
        return image

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["description"] = strip_tags(instance.description)
        return data


class CommentResponseSerializer(ModelSerializer):
    class Meta:
        model = CommentResponse
        exclude = "post",


class ProductLikeSerializer(ModelSerializer):
    class Meta:
        model = ProductLike
        fields = "__all__"


class ProductCommentSerializer(ModelSerializer):

    class Meta:
        model = ProductComment
        fields = "__all__"


class CartProductSerializer(ModelSerializer):

    content_object = ProductSerializer(read_only=True)

    class Meta:
        model = CartProduct
        exclude = "content_type", "object_id", "cart"


class CartSerializer(ModelSerializer):

    class Meta:
        model = Cart
        fields = "__all__"


class CommentLikeSerializer(ModelSerializer):

    class Meta:
        model = LikedComment
        fields = "__all__"


class CouponSerializer(ModelSerializer):

    class Meta:
        model = Coupon
        fields = "__all__"


class UserCouponSerializer(ModelSerializer):

    class Meta:
        model = UserCoupon
        fields = "__all__"


class UserOrderHistorySerializer(ModelSerializer):

    class Meta:
        model = UserOrderHistory
        fields = "__all__"


class UserSearchHistorySerializer(ModelSerializer):

    class Meta:
        model = UserSearchHistory
        fields = "__all__"
