from django.contrib import admin
from django.urls import path, include
from store.views import get_product_details, start_page

urlpatterns = [
    path('', start_page, name="home"),
    path("product/<slug:slug_id>", get_product_details, name="product")
]