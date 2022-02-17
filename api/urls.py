from django.urls import path, include
from .views import (
    DeleteCartView, ProductView,
    CommentResponseView, ProductLikeView,
    CartView, ProductCommentView,
    CommentLikeView,
    CouponView,
    UserCouponView,
    UserOrderHistoryView,
    UserSearchHistoryView
)

from .characteristic import urls as characteristic_urls

urlpatterns = [
    path("product/characteristics/", include(characteristic_urls)),
    path("get_products/", ProductView.as_view(), name="get_products"),
    path("get_products/<pk>/", ProductView.as_view(), name="get_one_product"),
    path("create_product/", ProductView.as_view(), name="create_product"),
    path("update_product/<pk>/", ProductView.as_view(), name="update_product"),
    path("delete_product/<pk>/", ProductView.as_view(), name="delete_product"),
    #
    # comment responce
    #
    path("product/<pk>/add_comment_response/",
         CommentResponseView.as_view(), name="add_comment_response"),
    path("product/<pk>/get_comments_response/",
         CommentResponseView.as_view(), name="get_comments"),
    path("product/<pk>/update_comment_response/<comment_pk>/",
         CommentResponseView.as_view(), name="update_comment_response"),
    path("product/<pk>/delete_comment_response/<comment_pk>/",
         CommentResponseView.as_view(), name="delete_comment_response"),
    #
    # comment products
    #
    path("product/<pk>/add_comment/",
         ProductCommentView.as_view(), name="add_comment"),
    path("product/<pk>/get_comments/",
         ProductCommentView.as_view(), name="get_comments"),
    path("product/<pk>/update_comment/<comment_pk>/",
         ProductCommentView.as_view(), name="update_comment"),
    path("product/<pk>/delete_comment/<comment_pk>/",
         ProductCommentView.as_view(), name="delete_comment"),
    #
    # comments likes
    #
    path("comment/<pk>/get_likes/",
         CommentLikeView.as_view(), name="get_likes"),
    path("comment/<pk>/add_likes/",
         CommentLikeView.as_view(), name="add_likes"),
    path("comment/<pk>/delete_like/<like_pk>/",
         CommentLikeView.as_view(), name="delete_like"),
    #
    # likes
    #
    path("product/<pk>/press_like/",
         ProductLikeView.as_view(), name="add_like"),
    path("product/<pk>/get_likes/",
         ProductLikeView.as_view(), name="get_likes"),
    path("product/<pk>/delete_like/<like_pk>/",
         ProductLikeView.as_view(), name="delete_like"),
    #
    # cart
    #
    path("get_cart/",
         CartView.as_view(), name="get_cart"),
    path("product/<pk>/add_to_cart/",
         CartView.as_view(), name="add_to_cart"),
    path("product/<pk>/remove_from_cart/<slug>",
         CartView.as_view(), name="remove_from_cart"),
    path("product/<pk>/remove_from_cart/<slug>/",
         CartView.as_view(), name="remove_from_cart_all"),
    path("delete_cart/", DeleteCartView.as_view(), name="delete_cart"),
    #
    # coupon
    #
    path("coupon/get_all/",
         CouponView.as_view(), name="get_coupones"),
    path("coupon/get_one/<pk>/",
         CouponView.as_view(), name="get_one_coupon"),
    path("coupon/add/",
         CouponView.as_view(), name="add_coupon"),
    path("coupon/update/<pk>/",
         CouponView.as_view(), name="update_coupon"),
    path("coupon/delete/<pk>/",
         CouponView.as_view(), name="delete_coupon"),
    #
    # user coupone
    #
    path("coupon/user/get_all/",
         UserCouponView.as_view(), name="get_user_coupones"),
    path("coupon/user/get_one/<pk>/",
         UserCouponView.as_view(), name="get_user_one_coupon"),
    path("coupon/user/add/<pk>/",
         UserCouponView.as_view(), name="add_user_coupon"),
    #
    # user search history
    #
    path("history/search/get_all/",
         UserSearchHistoryView.as_view(), name="get_user_search_history"),
    path("history/search/get_one/<pk>/",
         UserSearchHistoryView.as_view(), name="get_user_search_history_one"),
    path("history/search/add/",
         UserSearchHistoryView.as_view(), name="add_user_search_history"),
    #
    # user order history
    #
    path("history/order/get_all/",
         UserOrderHistoryView.as_view(), name="get_user_order_history"),
    path("history/order/get_one/<pk>/",
         UserOrderHistoryView.as_view(), name="get_user_order_history_one"),
    path("history/order/add/",
         UserOrderHistoryView.as_view(), name="add_user_order_history"),
]
