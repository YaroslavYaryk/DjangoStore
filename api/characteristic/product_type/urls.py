from django.urls import path
from .views import ProductTypeView


urlpatterns = [

    path("get_all/", ProductTypeView.as_view(), name="get_product_types"),
    path("get_one/<pk>/", ProductTypeView.as_view(), name="get_one_product_type"),
    path("update/<pk>/", ProductTypeView.as_view(), name="update_product_type"),
    path("create/", ProductTypeView.as_view(), name="create_product_type"),
    path("delete/<pk>/", ProductTypeView.as_view(), name="delete_product_type"),
]
