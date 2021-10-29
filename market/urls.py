
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.views import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("store.urls", namespace="")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()