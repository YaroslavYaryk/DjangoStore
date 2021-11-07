
from django.urls import path
from store.services.order import ProductLikesDown, ProductLikesUp, ProductNewest, ProductViewsDown, ProductViewsUp
from store.views import Category, Home, \
    SearchProduct, get_all_product_details, \
        get_product_featuress, get_product_photo, \
            get_product_reviews, get_product_video, likeView

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path("product/<slug:slug_id>/", get_all_product_details, name="read_more_about_all"),
    path("features/<slug:slug_id>", get_product_featuress, name="read_features"),
    path("reviews/<slug:slug_id>", get_product_reviews, name="read_reviews"),
    path("video/<slug:slug_id>", get_product_video, name="read_video"),
    path("photo/<slug:slug_id>", get_product_photo, name="read_photo"),
    path("<slug:product_id>/like/<slug:post_id>", likeView, name="like_product"),
    path("category/<slug:category_slug>", Category.as_view(), name="get_category"),
    path("search/", SearchProduct.as_view(), name="search_products"),
    path("sort_most_viewed_up/<str:place>", ProductViewsUp.as_view(), name="sort_most_viewed_up"),
    path("sort_most_viewed_down/<str:place>", ProductViewsDown.as_view(), name="sort_most_viewed_down"),
    path("sort_most_liked_down/<str:place>", ProductLikesDown.as_view(), name="sort_most_liked_down"),
    path("sort_most_liked_up/<str:place>", ProductLikesUp.as_view(), name="sort_most_liked_up"),
    path("sort_newest/<str:place>", ProductNewest.as_view(), name="sort_newest"),

]    
