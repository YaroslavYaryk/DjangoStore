from operator import imod
import re
from urllib import response
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils.text import slugify
from .characteristic.serializers import ProductCharacteristicSerializer
from rest_framework.decorators import api_view

from store.models import (
    Order,
    Product,
    CommentResponse,
    ProductCommentPhotos,
    ProductLike,
    LikedComment,
    UserSearchHistory,
    UserOrderHistory,
)
from .serializers import (
    OrderPostDeliveryTypeSerializer,
    OrderPostPaymentMethodsSerializer,
    OrderPostPlaceSerializer,
    OrderPostRecieverInfoSerializer,
    OrderPostSerializer,
    OrderPostWarehouseSerializer,
    OrderSerializer,
    ProductSerializer,
    ProductPostSerializer,
    ProductPostPutSerializer,
    CommentResponseSerializer,
    ProductLikeSerializer,
    CartProductSerializer,
    CartSerializer,
    ProductCommentSerializer,
    CommentLikeSerializer,
    CouponSerializer,
    ProductSimpleCommentSerializer,
    UserCouponSerializer,
    UserOrderHistorySerializer,
    UserSearchHistorySerializer,
    ProductCommentPostPutSerializer,
)
from .services.product import (
    get_comment_by_pk,
    get_coupon_by_pk,
    get_product_by_pk,
    get_photos,
)
from store.services.get_category import get_client_ip
from store.services.get_cart import *
from store.services.get_details import *
from .services import product


class ProductView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        if kwargs:
            queryset = Product.objects.get(pk=kwargs["pk"])
            serializer = ProductSerializer(queryset)
        else:
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductPostSerializer(data=request.data)
        if serializer.is_valid():
            if not serializer.validated_data.get("slug"):
                serializer.validated_data["slug"] = slugify(
                    serializer.validated_data.get("name")
                )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        post = Product.objects.get(pk=pk)
        serializer = ProductPostPutSerializer(instance=post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requset, pk):
        post = Product.objects.get(pk=pk)
        post.delete()
        return Response({"message": "Item was succesfully deleted"})


class ProductSpecCharacteristicView(APIView):
    def get(self, request, charact_type, slug):
        lookup = f"{charact_type}__slug"
        query = {lookup: slug}
        list_queryset = Characteristics.objects.filter(**query)
        ids = [el.product.id for el in list_queryset]
        queryset = Product.objects.filter(id__in=ids)

        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class CommentResponseView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        queryset = CommentResponse.objects.filter(post__pk=kwargs["pk"])
        serializer = CommentResponseSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, pk):

        serializer = CommentResponseSerializer(data=request.data)
        if serializer.is_valid():
            CommentResponse.objects.create(
                **serializer.data, post=get_product_by_pk(pk)
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, comment_pk):
        post = CommentResponse.objects.get(post__pk=pk, pk=comment_pk)
        serializer = CommentResponseSerializer(instance=post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requset, pk, comment_pk):
        post = CommentResponse.objects.get(post__pk=pk, pk=comment_pk)
        post.delete()
        return Response({"message": "Item was succesfully deleted"})


class ProductCommentView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        queryset = ProductComment.objects.filter(product__pk=kwargs["pk"], parent=None)
        serializer = ProductCommentSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request, pk):

        data = {
            **{
                "comment": request.data["comment"],
                "pros": request.data["pros"],
                "cons": request.data["cons"],
                "rating": int(request.data["rating"]),
                "parent": request.data.get("parent"),
            },
            "user": request.user.pk,
            "product": pk,
        }
        serializer = ProductCommentPostPutSerializer(data=data)
        if serializer.is_valid():
            instance = serializer.save()
            try:

                instance.photos.add(
                    ProductCommentPhotos.objects.create(photo=request.data["photo"])
                )
                instance.save()
            except:
                pass
            response = {
                **serializer.data,
                **get_photos(instance),
                "creation_date": instance.creation_date,
            }
            return Response(response, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, comment_pk):
        post = ProductComment.objects.get(product__pk=pk, pk=comment_pk)
        valid_request_data = product.get_valid_request_data(request.data)
        data = {**valid_request_data, "user": request.user.pk, "product": pk}
        serializer = ProductCommentPostPutSerializer(instance=post, data=data)

        if serializer.is_valid():
            instance = serializer.save()
            try:

                instance.photos.set(
                    [ProductCommentPhotos.objects.create(photo=request.data["photo"])]
                )
                instance.save()
                new_serializer = ProductCommentSerializer(instance=instance)
            except Exception as ex:
                print(ex)
            return Response(new_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requset, pk, comment_pk):
        post = ProductComment.objects.get(product__pk=pk, pk=comment_pk)

        serializer = ProductCommentSerializer(instance=post)
        data = {**serializer.data}
        post.delete()
        return Response(data)


class CommentLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        queryset = LikedComment.objects.filter(post_comment__pk=kwargs["pk"])
        serializer = CommentLikeSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request, pk):

        data = {**request.data, "post_comment": pk, "user": request.user.pk}

        serializer = CommentLikeSerializer(data=data)
        if serializer.is_valid():
            instance = LikedComment.objects.create(
                post_comment=get_comment_by_pk(pk), user=request.user
            )
            return Response(
                {
                    **serializer.data,
                    "id": instance.id,
                    "parent": instance.post_comment.parent.id
                    if instance.post_comment.parent
                    else None,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, like_pk):
        post = LikedComment.objects.get(post_comment__pk=pk, pk=like_pk)
        serializer = CommentLikeSerializer(instance=post)
        data = {
            **serializer.data,
            "id": post.id,
            "parent": post.post_comment.parent.id if post.post_comment.parent else None,
        }
        post.delete()
        return Response(data)


class UserCommentsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        queryset = ProductComment.objects.filter(user=request.user)
        serializer = ProductSimpleCommentSerializer(queryset, many=True)

        return Response(serializer.data)


class UserCommentLikesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        queryset = LikedComment.objects.filter(user=request.user)
        serializer = CommentLikeSerializer(queryset, many=True)

        return Response(serializer.data)


class ProductLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        queryset = ProductLike.objects.filter(post__pk=kwargs["pk"])
        serializer = ProductLikeSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request, pk):

        data = {**request.data, "user": request.user.pk, "post": pk}

        serializer = ProductLikeSerializer(data=data)
        if serializer.is_valid():
            product_like = ProductLike.objects.create(
                user=request.user, post=get_product_by_pk(pk)
            )
            return Response(
                {**serializer.data, "id": product_like.id},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requset, pk, like_pk):
        post = ProductLike.objects.get(post__pk=pk, pk=like_pk)
        post.delete()
        return Response({"message": "Item was succesfully deleted"})


class UserLikesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        queryset = ProductLike.objects.filter(user=request.user)
        serializer = ProductLikeSerializer(queryset, many=True)

        return Response(serializer.data)


from store.services.get_category import add_view_of_post, get_client_ip
from django.db.models import Q


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        queryset = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        try:
            cart = get_cart_by_request_user(request.user)
            product = Product.objects.get(pk=pk)
            cart_product = create_cart_product(request.user, cart, product)
            add_productcart_to_cart(request.user, cart, cart_product, product)
            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as er:
            print(er)
            return Response({"err": str(er)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, slug):
        try:
            cart = get_cart_by_request_user(request.user)
            product = Product.objects.get(pk=pk)
            cart_product = get_cart_product(user=request.user, product=product)
            if slug == "one":
                remove_product_from_cart(
                    cart, cart_product, request.user, product, True
                )
            else:
                remove_product_from_cart(cart, cart_product, request.user, product)
            # serializer = CartSerializer(cart)
            return Response({"message": "deleted"}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            print(str(ex))
            return Response({"err": str(ex)}, status=status.HTTP_400_BAD_REQUEST)


class DeleteCartView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):

        remove_all_from_cart_api(request.user)
        return Response({"message": "Cart was successfully unfilled"})


class CouponView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            queryset = Coupon.objects.get(pk=kwargs["pk"])
            serializer = CouponSerializer(queryset)
        else:
            queryset = Coupon.objects.all()
            serializer = CouponSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = CouponSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        post = Coupon.objects.get(pk=pk)
        serializer = CouponSerializer(instance=post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requset, pk):
        post = Coupon.objects.get(pk=pk)
        post.delete()
        return Response({"message": "Item was succesfully deleted"})


class UserCouponView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        if kwargs.get("pk"):
            queryset = UserCoupon.objects.get(pk=kwargs["pk"])
            serializer = UserCouponSerializer(queryset)
        else:
            queryset = UserCoupon.objects.all()
            serializer = UserCouponSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request, pk):

        data = {**request.data, "ip": get_client_ip(request), "coupon": pk}
        serializer = UserCouponSerializer(data=data)
        if serializer.is_valid():
            UserCoupon.objects.create(ip=data["ip"], coupon=get_coupon_by_pk(pk))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSearchHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        if kwargs.get("pk"):
            queryset = UserSearchHistory.objects.get(pk=kwargs["pk"])
            serializer = UserSearchHistorySerializer(queryset)
        else:
            queryset = UserSearchHistory.objects.all()
            serializer = UserSearchHistorySerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request):

        data = {**request.data, "ip": get_client_ip(request)}

        serializer = UserSearchHistorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserOrderHistoryView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):

        if kwargs.get("pk"):
            queryset = UserOrderHistory.objects.get(pk=kwargs["pk"])
            serializer = UserOrderHistorySerializer(queryset)
        else:
            queryset = UserOrderHistory.objects.all()
            serializer = UserOrderHistorySerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request):

        data = {**request.data, "ip": get_client_ip(request)}

        serializer = UserOrderHistorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductSearchFilterView(APIView):
    def post(self, request):
        pattern = request.data.get("pattern")
        filter_options = request.data.get("filter")
        search_queryset = product.search_queryset(pattern)
        filtered_queryset = product.handle_filter_queryset(
            search_queryset, filter_options
        )
        serializer = ProductSerializer(filtered_queryset, many=True)

        return Response(serializer.data)


class ProductCategoryFilterView(APIView):
    def post(self, request):
        pattern = request.data.get("pattern")
        filter_options = request.data.get("filter")
        search_queryset = product.category_queryset(pattern)
        filtered_queryset = product.handle_filter_queryset(
            search_queryset, filter_options
        )
        serializer = ProductSerializer(filtered_queryset, many=True)

        return Response(serializer.data)


class ProductCharacteristicFilterView(APIView):
    def post(self, request):
        pattern = request.data.get("pattern")
        filter_options = request.data.get("filter")
        search_queryset = product.characteristic_queryset(pattern)
        filtered_queryset = product.handle_filter_queryset(
            search_queryset, filter_options
        )
        serializer = ProductSerializer(filtered_queryset, many=True)

        return Response(serializer.data)


class SearchQueryAPIView(APIView):
    def get(self, request, pattern):
        search_keys = [
            y.strip()
            for x in Product.objects.all()
            for y in x.search_keys.split(",")
            if pattern.lower() in y.strip().lower()
        ]

        return Response({"data": search_keys})


class SearchProductsAPIView(APIView):
    def get(self, request, pattern):
        queryset = product.search_queryset(pattern)
        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)


class OrderAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        queryset = Order.objects.filter(owner=request.user)
        serializer = OrderSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request):
        print(request.data.get("cart"))
        data = {"owner": request.user.id, "cart": request.data.get("cart")}
        serializer = OrderPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages)


@api_view(["POST"])
def add_place_to_order(request):

    data = {"owner": request.user.id, **request.data}
    try:
        instance = Order.objects.get(owner=request.user, cart__id=data["cart"])
        serializer = OrderPostPlaceSerializer(data=data, instance=instance)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.error_messages)
    except Exception as ex:
        return Response({"error": str(ex)})


@api_view(["POST"])
def add_ware_house(request):

    data = {"owner": request.user.id, **request.data}
    try:
        instance = Order.objects.get(owner=request.user, cart__id=data["cart"])
        serializer = OrderPostWarehouseSerializer(data=data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages)
    except Exception as ex:
        return Response({"error": str(ex)})


@api_view(["POST"])
def add_delivery_type(request):

    data = {"owner": request.user.id, **request.data}
    try:
        instance = Order.objects.get(owner=request.user, cart__id=data["cart"])
        serializer = OrderPostDeliveryTypeSerializer(data=data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages)
    except Exception as ex:
        return Response({"error": str(ex)})


@api_view(["POST"])
def change_payment_methods(request):

    data = {"owner": request.user.id, **request.data}
    try:
        instance = Order.objects.get(owner=request.user, cart__id=data["cart"])
        serializer = OrderPostPaymentMethodsSerializer(data=data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages)
    except Exception as ex:
        return Response({"error": str(ex)})


@api_view(["POST"])
def add_order_coupon(request):
    try:
        instance = Order.objects.get(owner=request.user, cart__id=request.data["cart"])
        coupon = Coupon.objects.get(coupon_code=request.data["coupon"])
        instance.coupones.add(coupon)

        return Response({"operation": "Successfull"})
    except Exception as ex:
        return Response({"error": str(ex)})


@api_view(["DELETE"])
def discard_order(request, cart_id):
    try:
        instance = Order.objects.get(owner=request.user, cart__id=cart_id)
        instance.delete()
        return Response({"operation": "Successfull"})
    except Exception as ex:
        return Response({"error": str(ex)})


@api_view(["POST"])
def add_reciever_info(request):

    data = {"owner": request.user.id, **request.data}
    try:
        instance = Order.objects.get(owner=request.user, cart__id=data["cart"])
        serializer = OrderPostRecieverInfoSerializer(data=data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages)
    except Exception as ex:
        return Response({"error": str(ex)})


@api_view(["POST"])
def save_order(request):

    data = {"owner": request.user.id, **request.data}
    try:
        instance = Order.objects.get(owner=request.user, cart__id=data["cart"])
        instance.total_price = instance.cart.total_price
        instance.saved = True
        instance.save()
        return Response({"operation": "Successfull"})
    except Exception as ex:
        return Response({"error": str(ex)})
