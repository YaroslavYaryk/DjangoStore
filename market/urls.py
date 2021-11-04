from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from store.views import add_to_cart, delete_cart, get_cart, remove_from_cart, remove_one_product


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("store.urls", namespace="")),
    path("characteristic/", include("characteristics.urls", namespace="")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("cart/", get_cart, name="get_cart"),
    path("add_to_cart/<slug:product_slug>", add_to_cart, name="add_to_cart"),
    path("remove_from_cart/<slug:product_slug>", remove_from_cart, name="remove_from_cart"),
    path("remove_cart/", delete_cart, name="delete_cart"),
    path("remove_product/<slug:product_slug>/", remove_one_product, name="remove_one_product"), # quantity-1
    # url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
