from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    #
    # apps
    #
    path("", include("store.urls", namespace="")),
    path("users/", include("users.urls", namespace="")),
    path("characteristic/", include("characteristics.urls", namespace="")),
    path("api/", include("api.urls", namespace="")),
    #
    # serve
    #
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    #
    # features
    #
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("", include("social_django.urls", namespace="social")),
    #
    # django-rest
    #
    path("api-auth/", include("rest_framework.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    re_path(r"^auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.authtoken")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

handler404 = "store.views.handle_not_found"
handler500 = "store.views.handle_server_error"
handler400 = "store.views.handle_url_error"
handler403 = "store.views.handler_forbiden"
