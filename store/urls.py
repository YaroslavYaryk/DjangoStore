from django.urls import include
from django.contrib import admin
from django.urls import path
from store.views import Home, get_all_product_details, get_category, get_charact_diagonal_screen, get_product_featuress, get_product_photo, get_product_reviews, get_product_video, likeView

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path("product/<slug:slug_id>/", get_all_product_details, name="read_more_about_all"),
    path("features/<slug:slug_id>", get_product_featuress, name="read_features"),
    path("reviews/<slug:slug_id>", get_product_reviews, name="read_reviews"),
    path("video/<slug:slug_id>", get_product_video, name="read_video"),
    path("photo/<slug:slug_id>", get_product_photo, name="read_photo"),
    path("<slug:product_id>/like/<slug:post_id>", likeView, name="like_product"),
    path("category/<slug:category_slug>", get_category, name="get_category"),
    path("characteristic/", include("store.services.add_urls.urls", namespace="")),
    # path('screen_diagonal<slug:charact_slug>', get_charact_diagonal_screen, name="get_charact_diagonal_screen"),
]    
