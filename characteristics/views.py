from django.shortcuts import render
from django.views.generic.list import ListView
from store.services.get_home import get_order_dict, get_order_dict2
from store.services.order import get_place
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

        self.charact_slug = self.kwargs["charact_slug"]
        self.charact = self.kwargs["charact"]
        choice = self.request.GET.get("order")
        self.choice = get_place(self.request, choice) 
        return get_characteristic_query_according_to_character_field(self.charact_slug, self.request.user, self.charact, True, get_order_dict2().get(self.choice))[0]


    def get_context_data(self, *args, **kwargs):

        try:
            characteristic = get_characteristic_query_according_to_character_field(self.charact_slug, self.request.user, self.charact)
            character = characteristic[0]
            field_value = characteristic[1]
            
        except TypeError:
            character = None
            field_value = None
                        
        context = super().get_context_data(**kwargs)  # like dynamic list
        c_def = self.get_user_context(
            characteristic = character, 
            order = self.choice,
            title =  self.charact,
            cart = get_cart_by_user(self.request.user),
            field_value = field_value,
            charact_slug = self.charact_slug
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

