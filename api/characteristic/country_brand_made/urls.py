from django.urls import path
from .views import CountryBrandView, CountryMadeView


urlpatterns = [
    path("made/get_all/", CountryMadeView.as_view(), name="get_made_countries"),
    path("made/get_one/<pk>/", CountryMadeView.as_view(),
         name="get_one_made_country"),
    path("made/update/<pk>/", CountryMadeView.as_view(),
         name="update_made_country"),
    path("made/create/", CountryMadeView.as_view(), name="create_made_country"),
    path("made/delete/<pk>/", CountryMadeView.as_view(),
         name="delete_made_country"),
    path("brand/get_all/", CountryBrandView.as_view(), name="get_brand_countries"),
    path(
        "brand/get_one/<pk>/", CountryBrandView.as_view(), name="get_one_brand_country"
    ),
    path("brand/update/<pk>/", CountryBrandView.as_view(),
         name="update_brand_country"),
    path("brand/create/", CountryBrandView.as_view(),
         name="create_brand_country"),
    path("brand/delete/<pk>/", CountryBrandView.as_view(),
         name="delete_brand_country"),
]
