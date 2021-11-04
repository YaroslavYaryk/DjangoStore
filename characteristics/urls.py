from django.urls import include
from django.urls import path
from characteristics.views import get_characteristic_query

urlpatterns = [
    path('<str:charact>/<slug:charact_slug>', get_characteristic_query, name="get_characteristic_query"),
]    
