from django.shortcuts import render

from store.services.get_details import get_characteristic_query_according_to_character_field
from store.services.get_cart import get_cart_by_user
# Create your views here.


def get_characteristic_query(request, charact,  charact_slug):
    """get products by diagonal screen"""

    characteristic = get_characteristic_query_according_to_character_field(charact_slug, request.user, charact)
    
    context = {
        "characteristic" : characteristic[0], 
        "title" : charact,
        "cart": get_cart_by_user(request.user),
        'field_value' : characteristic[1]
    }

    return render(request, "store/characteristics/characteristic_query.html", context=context)

