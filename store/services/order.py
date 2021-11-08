
from django.views.generic.list import ListView
from store.services.get_category import get_client_ip
from store.services.get_home import get_dict_all_products_like
from store.models import Product, UserOrderHistory
from store.utils import DataMixin
from loguru import logger as log


log.add("/home/yaroslav/Programming/Python/Django/StoreProject/market/logging/log3.log",
        enqueue=True, level="DEBUG", rotation="10 MB")


def get_place(request, order_place):

    try:
        if order_place:
            UserOrderHistory.objects.create(ip=get_client_ip(request), order_place=order_place)
        else:
            order_place = UserOrderHistory.objects.filter(ip = get_client_ip(request)).last().order_place
            if not order_place:
                raise Exception 
    except Exception:
        order_place = "newest" 
    finally:
        return order_place


class ProductViewsUp(DataMixin, ListView):
    model = Product
    template_name = "market/order.html"
    context_object_name = 'all_products'
    
    def get_queryset(self):

        place = self.kwargs.get("place")
        self.place = get_place(self.request, place) 
        if self.place == "home":
            return Product.objects.order_by("ip")


    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(**kwargs)  # like dynamic list
        c_def = self.get_user_context(
            place=self.place,
            title="most_viewed_up",
            order = "most popular 👆",
            all_products_like=get_dict_all_products_like(self.request.user))
        return dict(list(context.items()) + list(c_def.items()))


class ProductViewsDown(DataMixin, ListView):
    model = Product
    # success_url = reverse_lazy("home")
    template_name = "market/order.html"
    context_object_name = 'all_products'
    
    def get_queryset(self):

        print(self.request.session.session_key)

        place = self.kwargs.get("place")
        self.place = get_place(self.request, place)
        if self.place == "home":
            return Product.objects.order_by("-ip")


    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(**kwargs)  # like dynamic list
        c_def = self.get_user_context(
            place=self.place,
            title="most_viewed_down",
            order = "most popular 👇",
            all_products_like=get_dict_all_products_like(self.request.user))
        return dict(list(context.items()) + list(c_def.items()))


class ProductLikesDown(DataMixin, ListView):
    model = Product
    # success_url = reverse_lazy("home")
    template_name = "market/order.html"
    context_object_name = 'all_products'
    
    def get_queryset(self):

        place = self.kwargs.get("place")
        self.place = get_place(self.request, place)
        if self.place == "home":
            return Product.objects.order_by("-likes")


    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(**kwargs)  # like dynamic list
        c_def = self.get_user_context(
            place=self.place,
            title="most_liked_down",
            order = "most liked 👇",
            all_products_like=get_dict_all_products_like(self.request.user))
        return dict(list(context.items()) + list(c_def.items()))


class ProductLikesUp(DataMixin, ListView):
    model = Product
    # success_url = reverse_lazy("home")
    template_name = "market/order.html"
    context_object_name = 'all_products'
    
    def get_queryset(self):

        place = self.kwargs.get("place")
        self.place = get_place(self.request, place)
        if self.place == "home":
            return Product.objects.order_by("likes")


    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(**kwargs)  # like dynamic list
        c_def = self.get_user_context(
            place=self.place,
            title="most_liked_up",
            order = "most liked 👆",
            all_products_like=get_dict_all_products_like(self.request.user))
        return dict(list(context.items()) + list(c_def.items()))        



class ProductNewest(DataMixin, ListView):
    model = Product
    # success_url = reverse_lazy("home")
    template_name = "market/order.html"
    context_object_name = 'all_products'
    
    def get_queryset(self):

        place = self.kwargs.get("place")
        self.place = get_place(self.request, place)
        if self.place == "home":
            return Product.objects.all()


    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(**kwargs)  # like dynamic list
        c_def = self.get_user_context(
            place=self.place,
            title="newest",
            order = "newest",
            all_products_like=get_dict_all_products_like(self.request.user))
        return dict(list(context.items()) + list(c_def.items()))                