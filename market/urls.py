
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from store.views import add_to_cart, get_cart


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("store.urls", namespace="")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("cart/", get_cart, name="get_cart"),
    path("add_to_cart/<slug:product_slug>", add_to_cart, name="add_to_cart")
    # url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
