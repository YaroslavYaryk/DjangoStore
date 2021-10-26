from django.contrib import admin
from django.urls import path, include
from store.views import start_page

urlpatterns = [
    path('', start_page, name="home"),
]