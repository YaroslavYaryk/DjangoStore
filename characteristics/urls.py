from django.urls import include
from django.urls import path
from characteristics.views import ProductsByCharacteristic

urlpatterns = [
    path('<str:charact>/<slug:charact_slug>', ProductsByCharacteristic.as_view() , name="get_characteristic_query"),
]    
