from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from store.views import LoginUser, LogoutUser, ProfileView, RegisterUser, add_to_cart, delete_cart, get_cart, get_information_about, remove_from_cart, remove_one_product
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("store.urls", namespace="")),
    path("characteristic/", include("characteristics.urls", namespace="")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("cart/", get_cart, name="get_cart"),
    path("add_to_cart/<slug:product_slug>", add_to_cart, name="add_to_cart"),
    path("remove_from_cart/<slug:product_slug>",
         remove_from_cart, name="remove_from_cart"),
    path("remove_cart/", delete_cart, name="delete_cart"),
    path("remove_product/<slug:product_slug>/", remove_one_product,
         name="remove_one_product"),  # quantity-1
    path("sign_in/", LoginUser.as_view(), name="sign_in"),
    path("register/", (RegisterUser.as_view()), name="register"),
    path("about/", get_information_about, name="about"),

    path("accounts/profile/", ProfileView.as_view(), name="profile"),
    path("logout/<slug:admin_name>", LogoutUser.as_view(), name="logout"),
    path("accounts/password_reset/",
         auth_views.PasswordResetView.as_view(), name="reset_password"),
    path("accounts/password_reset_sent/",
         auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("accounts/reset/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("accounts/password_reset_complete/",
         auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('accounts/password_change/', PasswordChangeView.as_view(
          template_name='registration/password_change_form.html'),
          name='password_change'),
    path('accounts/password_change/done/',
          PasswordChangeDoneView.as_view(
          template_name='registration/password_change_done.html'),
          name='password_change_done'),
    # path("logout/<slug:admin_name>", LogoutUser.as_view(), name="logout"),
#     url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    path('', include('social_django.urls', namespace='social')),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()


handler404 = "store.views.handle_not_found"
handler500 = "store.views.handle_server_error"
handler400 = "store.views.handle_url_error"
handler403 = "store.views.handler_forbiden"