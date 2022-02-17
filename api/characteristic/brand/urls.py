from django.urls import path
from .views import BrandView


urlpatterns = [
    path("get_all/", BrandView.as_view(), name="get_brands"),
    path("get_one/<pk>/", BrandView.as_view(), name="get_one_brand"),
    path("update/<pk>/", BrandView.as_view(), name="update_brand"),
    path("create/", BrandView.as_view(), name="create_brand"),
    path("delete/<pk>/", BrandView.as_view(), name="delete_brand"),
]
