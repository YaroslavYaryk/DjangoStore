
from django.urls import path
from store.services.get_home import send_mail_register
from store.views import (
    Category, Home,
    SearchProduct, add_to_cart,
    delete_cart, get_all_product_details,
    get_cart, get_product_featuress,
    get_product_photo, get_product_reviews,
    get_product_video, likeCommentView,
    likeView, get_information_about,
    remove_from_cart, remove_one_product,
    get_cart, add_to_cart, remove_from_cart,
    delete_cart, remove_one_product
)
urlpatterns = [
    path("about/", get_information_about, name="about"),
    path('', Home.as_view(), name="home"),
    path("product/<slug:slug_id>/", get_all_product_details,
         name="read_more_about_all"),
    path("features/<slug:slug_id>/", get_product_featuress, name="read_features"),
    path("reviews/<slug:slug_id>/", get_product_reviews, name="read_reviews"),
    path("video/<slug:slug_id>/", get_product_video, name="read_video"),
    path("photo/<slug:slug_id>/", get_product_photo, name="read_photo"),
    path("<slug:product_id>/<slug:cat>/like/<slug:post_id>/",
         likeView, name="like_product"),
    path("<slug:product_id>/like_comment/<int:comment_pk>/",
         likeCommentView, name="comment_like"),
    path("category/<slug:category_slug>/",
         Category.as_view(), name="get_category"),
    path("search/", SearchProduct.as_view(), name="search_products"),
    path("send_message/", send_mail_register, name="send_message_to_user"),
    path("cart/", get_cart, name="get_cart"),
    path("add_to_cart/<slug:product_slug>", add_to_cart, name="add_to_cart"),
    path("remove_from_cart/<slug:product_slug>",
         remove_from_cart,
         name="remove_from_cart"),
    path("remove_cart/", delete_cart, name="delete_cart"),
    path("remove_product/<slug:product_slug>/",
         remove_one_product,
         name="remove_one_product"),  # quantity-1

]
