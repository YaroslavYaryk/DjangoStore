from copyreg import constructor
from dataclasses import fields
import json
import html_to_json
from rest_framework.serializers import ModelSerializer
from store.models import (
    Product,
    ProductComment,
    CommentResponse,
    ProductLike,
    CartProduct,
    Cart,
    LikedComment,
    Coupon,
    UserCoupon,
    UserOrderHistory,
    UserSearchHistory,
    ProductImage,
    Order,
)
from decouple import config
from math import floor
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
from users.api.serializers import UserSerializer
from users.services import users as user_services
from django.contrib.admin.options import get_content_type_for_model
from django.contrib.contenttypes.models import ContentType
from decouple import config
from .services.product import get_likesCount


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
    description = SerializerMethodField()
    comment_count = SerializerMethodField()
    rating = SerializerMethodField()

    photos = SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_photo(self, instance):
        try:
            image = f"{config('USERHOST')}:{config('USERPORT')}{instance.photo.url}"
        except Exception:
            image = None
        return image

    def get_description(self, instance):
        print(type(instance.description))
        return instance.description

    def get_photos(self, instance):

        return [
            f"{config('USERHOST')}:{config('USERPORT')}{el.images.url}"
            for el in ProductImage.objects.filter(product=instance)
        ]

    def get_comment_count(self, instance):
        return ProductComment.objects.filter(product=instance).count()

    def get_rating(self, instance):
        query = ProductComment.objects.filter(product=instance)
        try:
            return floor(sum(el.rating for el in query) / query.count())
        except ZeroDivisionError:
            return 0

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data["description"] = strip_tags(instance.description)
    #     return data


class CommentResponseSerializer(ModelSerializer):
    class Meta:
        model = CommentResponse
        exclude = ("post",)


class ProductLikeSerializer(ModelSerializer):
    class Meta:
        model = ProductLike
        fields = "__all__"


class ProductCommentPostPutSerializer(ModelSerializer):
    class Meta:
        model = ProductComment
        exclude = ("photos", "creation_date")


class ProductSimpleCommentSerializer(ModelSerializer):

    user = SerializerMethodField()

    class Meta:
        model = ProductComment
        fields = ("id", "product", "user")

    def get_user(self, instance):
        return instance.user.id


class ProductCommentSerializer(ModelSerializer):

    photos = SerializerMethodField()
    user = UserSerializer()
    comment_likes = SerializerMethodField()
    replies = SerializerMethodField()
    creation_date = SerializerMethodField()

    class Meta:
        model = ProductComment
        fields = "__all__"

    def get_photos(self, instance):
        return [
            {
                "id": el.id,
                "url": f"{config('USERHOST')}:{config('USERPORT')}{el.photo.url}",
            }
            for el in instance.photos.all()
        ]

    def get_comment_likes(self, instance):
        return LikedComment.objects.filter(post_comment=instance).count()

    def get_replies(self, instance):
        return [
            {
                "id": el.id,
                "comment": el.comment,
                "date": el.creation_date.isoformat(),
                "comment_id": el.parent.id,
                # "username": user_services.get_user_by_id(el.user_id).username,
                "user": {
                    "id": user_services.get_user_by_id(el.user_id).id,
                    "username": user_services.get_user_by_id(el.user_id).username,
                    "email": user_services.get_user_by_id(el.user_id).email,
                    "first_name": user_services.get_user_by_id(el.user_id).first_name,
                    "last_name": user_services.get_user_by_id(el.user_id).last_name,
                    "middle_name": user_services.get_user_by_id(el.user_id).middle_name,
                    "living_place": user_services.get_user_by_id(
                        el.user_id
                    ).living_place,
                    "ware_house": user_services.get_user_by_id(el.user_id).ware_house,
                    "delivery_type": user_services.get_user_by_id(
                        el.user_id
                    ).delivery_type,
                    "phone": user_services.get_user_by_id(el.user_id).phone,
                },
                "date": el.creation_date,
                "photos": [
                    {
                        "id": elem.id,
                        "url": f"{config('USERHOST')}:{config('USERPORT')}{elem.photo.url}",
                    }
                    for elem in el.photos.all()
                ],
                "rating": el.rating,
                "comment_likes": get_likesCount(el),
            }
            for el in instance.children()
        ]

    def get_creation_date(self, instance):
        return instance.creation_date.isoformat()


class CartProductSerializer(ModelSerializer):

    content_object = ProductSerializer(read_only=True)
    content_object = SerializerMethodField()

    class Meta:
        model = CartProduct
        exclude = "content_type", "object_id", "cart"

    def get_content_object(self, instance):
        print(instance.cart.products.all(), 1)
        return "a"


class CartSerializer(ModelSerializer):

    products = SerializerMethodField()

    class Meta:
        model = Cart
        fields = "__all__"

    @staticmethod
    def get_product_count(product, instance):
        try:
            return instance.products.get(id=product).quantity
        except:
            return 0

    @staticmethod
    def get_product(id):
        return Product.objects.get(pk=id)

    def get_products(self, instance):

        return [
            {
                "productId": self.get_product(el.object_id).id,
                "fullName": self.get_product(el.object_id).name,
                "image": f"{config('USERHOST')}:{config('USERPORT')}{self.get_product(el.object_id).photo.url}",
                "count": self.get_product_count(el.id, instance),
                "price": self.get_product(el.object_id).price,
            }
            for el in instance.products.all()
        ]


class CommentLikeSerializer(ModelSerializer):
    comment_parent = SerializerMethodField()

    class Meta:
        model = LikedComment
        fields = "__all__"

    def get_comment_parent(self, instance):
        try:
            return (
                instance.post_comment.parent.id
                if instance.post_comment.parent
                else None
            )
        except:
            return None


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


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderPostSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ("owner", "cart")


class OrderPostPlaceSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ("owner", "cart", "place_id", "place")


class OrderPostWarehouseSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ("owner", "cart", "ware_house_id", "ware_house_name", "place_id")


class OrderPostDeliveryTypeSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ("owner", "cart", "delivery_type")


class OrderPostPaymentMethodsSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ("owner", "cart", "price_method")


class OrderPostRecieverInfoSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "owner",
            "cart",
            "reciever_first_name",
            "reciever_last_name",
            "reciever_middle_name",
            "reciever_phone",
        )
