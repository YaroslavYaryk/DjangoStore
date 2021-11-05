from django.shortcuts import render
from django.views.generic.list import ListView
from characteristics.services.category_characteristic import get_queryset_for_all_characteristic
from store.models import Product
from store.utils import DataMixin

from store.services.get_details import get_characteristic_query_according_to_character_field
from store.services.get_cart import get_cart_by_user
# Create your views here.


class ProductsByCharacteristic(DataMixin ,ListView):
    model = Product
    # success_url = reverse_lazy("home")
    template_name = "store/characteristics/characteristic_query.html"
    context_object_name = 'products'

    def get_queryset(self):

        charact_slug = self.kwargs["charact_slug"]
        charact = self.kwargs["charact"]
        return get_characteristic_query_according_to_character_field(charact_slug, self.request.user, charact, True)


    def get_context_data(self, *args, **kwargs):

        charact_slug = self.kwargs["charact_slug"]
        charact = self.kwargs["charact"]
        characteristic = get_characteristic_query_according_to_character_field(charact_slug, self.request.user, charact)
        if characteristic:
            character = characteristic[0]
            field_value = characteristic[1]
        else:
            character = None
            field_value = None    
        context = super().get_context_data(**kwargs)  # like dynamic list
        c_def = self.get_user_context(
            characteristic = character, 
            title =  charact,
            cart = get_cart_by_user(self.request.user),
            field_value = field_value,
        )
        return dict(list(context.items()) + list(c_def.items()))





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

