from django.urls import include
from django.urls import path

from store.views import get_charact_diagonal_screen

urlpatterns = [
    path('screen_diagonal<slug:charact_slug>', get_charact_diagonal_screen, name="get_charact_diagonal_screen"),
]    
