from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView
from django.urls import re_path, path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    CreateUserAPIView,
    LogoutUserAPIView,
    UserApiView,
    CustomAuthToken,
    UserEditBaseAPIView,
)


urlpatterns = [
    path("create/", CustomUserCreate.as_view(), name="create_user"),
    path("logout/blacklist/", BlacklistTokenUpdateView.as_view(), name="blacklist"),
    re_path(r"^auth/login/$", CustomAuthToken.as_view(), name="auth_user_login"),
    re_path(r"^auth/register/$", CreateUserAPIView.as_view(), name="auth_user_create"),
    re_path(r"^auth/logout/$", LogoutUserAPIView.as_view(), name="auth_user_logout"),
    path("user_profile/", UserApiView.as_view(), name="user_profile"),
    path("user_base_edit/", UserEditBaseAPIView.as_view(), name="user_base_edit"),
]
