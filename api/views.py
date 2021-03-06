from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils.text import slugify

from store.models import Product, CommentResponse, ProductLike, LikedComment, UserSearchHistory, UserOrderHistory
from .serializers import (
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
    UserCouponSerializer,
    UserOrderHistorySerializer,
    UserSearchHistorySerializer
)
from .services.product import get_comment_by_pk, get_coupon_by_pk, get_product_by_pk
from store.services.get_category import get_client_ip
from store.services.get_cart import *
from store.services.get_details import *


class ProductView(APIView):
    permission_classes = [IsAuthenticated]

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


class CommentResponseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        queryset = CommentResponse.objects.filter(post__pk=kwargs["pk"])
        serializer = CommentResponseSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, pk):

        serializer = CommentResponseSerializer(data=request.data)
        if serializer.is_valid():
            CommentResponse.objects.create(
                **serializer.data, post=get_product_by_pk(pk))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, comment_pk):
        post = CommentResponse.objects.get(post__pk=pk, pk=comment_pk)
        serializer = CommentResponseSerializer(
            instance=post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requset, pk, comment_pk):
        post = CommentResponse.objects.get(post__pk=pk, pk=comment_pk)
        post.delete()
        return Response({"message": "Item was succesfully deleted"})


class ProductCommentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        queryset = ProductComment.objects.filter(product__pk=kwargs["pk"])
        serializer = ProductCommentSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request, pk):

        data = {**request.data, "user": request.user.pk,
                "product": pk}
        serializer = ProductCommentSerializer(data=data)
        if serializer.is_valid():
            ProductComment.objects.create(
                comment=serializer.data["comment"], product=get_product_by_pk(pk), user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, comment_pk):
        post = ProductComment.objects.get(product__pk=pk, pk=comment_pk)
        serializer = ProductCommentSerializer(
            instance=post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requset, pk, comment_pk):
        post = ProductComment.objects.get(product__pk=pk, pk=comment_pk)
        post.delete()
        return Response({"message": "Item was succesfully deleted"})


class CommentLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        queryset = LikedComment.objects.filter(post_comment__pk=kwargs["pk"])
        serializer = CommentLikeSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request, pk):

        data = {**request.data, "post_comment": pk,
                "user": request.user.pk}

        serializer = CommentLikeSerializer(data=data)
        if serializer.is_valid():
            LikedComment.objects.create(
                post_comment=get_comment_by_pk(pk), user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requset, pk, like_pk):
        post = LikedComment.objects.get(post_comment__pk=pk, pk=like_pk)
        post.delete()
        return Response({"message": "Item was succesfully deleted"})


class ProductLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        queryset = ProductLike.objects.filter(post__pk=kwargs["pk"])
        serializer = ProductLikeSerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request, pk):

        data = {**request.data, "user": request.user.pk,
                "post": pk}

        serializer = ProductLikeSerializer(data=data)
        if serializer.is_valid():
            print(request.user)
            ProductLike.objects.create(
                user=request.user, post=get_product_by_pk(pk))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, requset, pk, like_pk):
        post = ProductLike.objects.get(post__pk=pk, pk=like_pk)
        post.delete()
        return Response({"message": "Item was succesfully deleted"})


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        queryset = CartProduct.objects.filter(user=get_client_ip(request))
        serializer = CartProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        try:
            ip = get_client_ip(request)
            cart = get_cart_by_user(ip)
            product = Product.objects.get(pk=pk)
            cart_product = create_cart_product(ip, cart, product)
            add_productcart_to_cart(ip, cart, cart_product, product)
            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as er:
            return Response({"err": er}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, slug):
        try:
            ip = get_client_ip(request)
            cart = get_cart_by_user(ip)
            product = Product.objects.get(pk=pk)
            cart_product = get_cart_product(user=ip, product=product)
            if slug == "one":
                remove_product_from_cart(cart, cart_product, ip, product, True)
            else:
                remove_product_from_cart(cart, cart_product, ip, product)
            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({"err": ex}, status=status.HTTP_400_BAD_REQUEST)


class DeleteCartView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):

        ip = get_client_ip(request)
        remove_all_from_cart(ip)
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
        serializer = CouponSerializer(
            instance=post, data=request.data)

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

        data = {**request.data, "ip": get_client_ip(request),
                "coupon": pk}
        serializer = UserCouponSerializer(data=data)
        if serializer.is_valid():
            UserCoupon.objects.create(
                ip=data["ip"], coupon=get_coupon_by_pk(pk))
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
