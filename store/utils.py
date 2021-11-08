from django.contrib import messages
from store.services.get_category import get_client_ip
from store.services.get_cart import get_cart_by_user


class DataMixin(object):

    """Mixin for all clases that we have to
    make they shorter and fater"""
    paginate_by = 12   #needs to be queryset in function(not import tegs '{% load menu_tags %}' )  

    
    def __init__(self) -> None:
        
        self.order_list = ["newest", "most popular 👇",
                    "most popular 👆", "price 👆", "price 👇"]

    def get_user_context(self, *args, **kwargs):
        ip = get_client_ip(self.request)
        context = kwargs
        context["cart"] = get_cart_by_user(ip)
        context["order_list"] = self.order_list
        return context

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)     