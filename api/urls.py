from django.urls import path, include
from .views import (
    DeleteCartView,
    ProductView,
    CommentResponseView,
    ProductLikeView,
    CartView,
    ProductCommentView,
    CommentLikeView,
    CouponView,
    UserCommentLikesView,
    UserCouponView,
    UserOrderHistoryView,
    UserSearchHistoryView,
    ProductSpecCharacteristicView,
    UserLikesView,
    ProductSearchFilterView,
    ProductCategoryFilterView,
    ProductCharacteristicFilterView,
    SearchQueryAPIView,
    SearchProductsAPIView,
    UserCommentsView,
    OrderAPIView,
    add_delivery_type,
    add_order_coupon,
    add_place_to_order,
    add_reciever_info,
    add_ware_house,
    change_payment_methods,
    discard_order,
    save_order,
)

from .characteristic import urls as characteristic_urls

urlpatterns = [
    path("product/characteristics/", include(characteristic_urls)),
    path("get_products/", ProductView.as_view(), name="get_products"),
    path("get_products/<pk>/", ProductView.as_view(), name="get_one_product"),
    path("create_product/", ProductView.as_view(), name="create_product"),
    path("update_product/<pk>/", ProductView.as_view(), name="update_product"),
    path("delete_product/<pk>/", ProductView.as_view(), name="delete_product"),
    path(
        "specific_characteristics/<charact_type>/<slug>/",
        ProductSpecCharacteristicView.as_view(),
        name="specific_characteristics",
    ),
    path("product_search/", ProductSearchFilterView.as_view(), name="product_search"),
    path(
        "product_categories/",
        ProductCategoryFilterView.as_view(),
        name="product_categories",
    ),
    path(
        "product_characteristic/",
        ProductCharacteristicFilterView.as_view(),
        name="product_characteristic",
    ),
    path("search_query/<pattern>/", SearchQueryAPIView.as_view(), name="search_query"),
    path(
        "search_product/<pattern>/",
        SearchProductsAPIView.as_view(),
        name="search_product",
    ),
    #
    # comment responce
    #
    path(
        "product/<pk>/add_comment_response/",
        CommentResponseView.as_view(),
        name="add_comment_response",
    ),
    path(
        "product/<pk>/get_comments_response/",
        CommentResponseView.as_view(),
        name="get_comments",
    ),
    path(
        "product/<pk>/update_comment_response/<comment_pk>/",
        CommentResponseView.as_view(),
        name="update_comment_response",
    ),
    path(
        "product/<pk>/delete_comment_response/<comment_pk>/",
        CommentResponseView.as_view(),
        name="delete_comment_response",
    ),
    #
    # comment products
    #
    path("product/<pk>/add_comment/", ProductCommentView.as_view(), name="add_comment"),
    path(
        "product/<pk>/get_comments/", ProductCommentView.as_view(), name="get_comments"
    ),
    path(
        "product/<pk>/update_comment/<comment_pk>/",
        ProductCommentView.as_view(),
        name="update_comment",
    ),
    path(
        "product/<pk>/delete_comment/<comment_pk>/",
        ProductCommentView.as_view(),
        name="delete_comment",
    ),
    path("user_comments/", UserCommentsView.as_view(), name="user_comments"),
    #
    # comments likes
    #
    path("comment/<pk>/get_likes/", CommentLikeView.as_view(), name="get_likes"),
    path("comment/<pk>/add_like/", CommentLikeView.as_view(), name="add_likes"),
    path(
        "comment/<pk>/delete_like/<like_pk>/",
        CommentLikeView.as_view(),
        name="delete_like",
    ),
    path(
        "comment/user_likes/", UserCommentLikesView.as_view(), name="user_comment_likes"
    ),
    #
    # likes
    #
    path("product/<pk>/press_like/", ProductLikeView.as_view(), name="add_like"),
    path("product/<pk>/get_likes/", ProductLikeView.as_view(), name="get_likes"),
    path(
        "product/<pk>/delete_like/<like_pk>/",
        ProductLikeView.as_view(),
        name="delete_like",
    ),
    path("user_likes/", UserLikesView.as_view(), name="user_likes"),
    #
    # cart
    #
    path("get_cart/", CartView.as_view(), name="get_cart_api"),
    path("product/<pk>/add_to_cart/", CartView.as_view(), name="add_to_cart"),
    path(
        "product/<pk>/remove_from_cart/<slug>/",
        CartView.as_view(),
        name="remove_from_cart",
    ),
    path(
        "product/<pk>/remove_from_cart/<slug>/",
        CartView.as_view(),
        name="remove_from_cart_all",
    ),
    path("delete_cart/", DeleteCartView.as_view(), name="delete_cart_api"),
    #
    # coupon
    #
    path("coupon/get_all/", CouponView.as_view(), name="get_coupones"),
    path("coupon/get_one/<pk>/", CouponView.as_view(), name="get_one_coupon"),
    path("coupon/add/", CouponView.as_view(), name="add_coupon"),
    path("coupon/update/<pk>/", CouponView.as_view(), name="update_coupon"),
    path("coupon/delete/<pk>/", CouponView.as_view(), name="delete_coupon"),
    #
    # user coupone
    #
    path("coupon/user/get_all/", UserCouponView.as_view(), name="get_user_coupones"),
    path(
        "coupon/user/get_one/<pk>/",
        UserCouponView.as_view(),
        name="get_user_one_coupon",
    ),
    path("coupon/user/add/<pk>/", UserCouponView.as_view(), name="add_user_coupon"),
    #
    # user search history
    #
    path(
        "history/search/get_all/",
        UserSearchHistoryView.as_view(),
        name="get_user_search_history",
    ),
    path(
        "history/search/get_one/<pk>/",
        UserSearchHistoryView.as_view(),
        name="get_user_search_history_one",
    ),
    path(
        "history/search/add/",
        UserSearchHistoryView.as_view(),
        name="add_user_search_history",
    ),
    #
    # user order history
    #
    path(
        "history/order/get_all/",
        UserOrderHistoryView.as_view(),
        name="get_user_order_history",
    ),
    path(
        "history/order/get_one/<pk>/",
        UserOrderHistoryView.as_view(),
        name="get_user_order_history_one",
    ),
    path(
        "history/order/add/",
        UserOrderHistoryView.as_view(),
        name="add_user_order_history",
    ),
    # order
    path("orders/all/", OrderAPIView.as_view(), name="OrderAPIView"),
    path("orders/add/", OrderAPIView.as_view(), name="AddOrderAPIView"),
    path("orders/add_place/", add_place_to_order, name="add_place_to_order"),
    path("orders/add_warehouse/", add_ware_house, name="add_ware_house"),
    path(
        "orders/add_delivery_type/", add_delivery_type, name="add_delivery_type_house"
    ),
    path(
        "orders/change_payment_methods/",
        change_payment_methods,
        name="change_payment_methods",
    ),
    path("orders/add_coupon/", add_order_coupon, name="add_order_coupon"),
    path("orders/discard/<cart_id>/", discard_order, name="discard_order"),
    path("orders/add_reciever_info/", add_reciever_info, name="add_reciever_info"),
    path("orders/save/", save_order, name="save_order"),
]
