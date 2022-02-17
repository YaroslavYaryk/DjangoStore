from django.urls import path
from .views import ScreenDiagonalView, ScreenTypeView, ScreenFrequencyView


urlpatterns = [
    path(
        "get_screen_diagonal/<pk>",
        ScreenDiagonalView.as_view(),
        name="get_diagonal_screen",
    ),
    path(
        "get_screen_diagonal/",
        ScreenDiagonalView.as_view(),
        name="get_diagonal_screens",
    ),
    path(
        "create_screen_diagonal/",
        ScreenDiagonalView.as_view(),
        name="create_diagonal_screen",
    ),
    path(
        "update_screen_diagonal/<pk>/",
        ScreenDiagonalView.as_view(),
        name="update_screen_diagonal",
    ),
    path(
        "delete_screen_diagonal/<pk>/",
        ScreenDiagonalView.as_view(),
        name="delete_screen_diagonal",
    ),
    # screen type
    path("get_screen_type/<pk>", ScreenTypeView.as_view(), name="get_screen_type"),
    path("get_screen_type/", ScreenTypeView.as_view(), name="get_screen_types"),
    path("create_screen_type/", ScreenTypeView.as_view(),
         name="create_screen_type"),
    path(
        "update_screen_type/<pk>/", ScreenTypeView.as_view(), name="update_screen_type"
    ),
    path(
        "delete_screen_type/<pk>/", ScreenTypeView.as_view(), name="delete_screen_type"
    ),
    # screen freequency
    path(
        "get_screen_frequency/<pk>/",
        ScreenFrequencyView.as_view(),
        name="get_screen_frequency",
    ),
    path(
        "get_screen_frequency/",
        ScreenFrequencyView.as_view(),
        name="get_screen_frequencies",
    ),
    path(
        "create_screen_frequency/",
        ScreenFrequencyView.as_view(),
        name="create_screen_frequency",
    ),
    path(
        "update_screen_frequency/<pk>/",
        ScreenFrequencyView.as_view(),
        name="update_screen_frequency",
    ),
    path(
        "delete_screen_frequency/<pk>/",
        ScreenFrequencyView.as_view(),
        name="delete_screen_frequency",
    ),
]
