from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic import ListView
from store.utils import DataMixin
from store.services.get_cart import add_productcart_to_cart, create_cart_product, get_cart_by_user, get_cart_product, remove_product_from_cart
from store.services.get_home import get_dict_all_products_like, get_path_to_redirect
from store.models import  Cart, CartProduct, Product
from store.services.get_details import check_if_post_like_and_get_count, get_all_aditional_image_by_slug_id, get_dict_aditional_like, \
    get_header_menu, get_list_of_special, get_special_product, press_like_to_product, set_cookies_for_product_like


# Create your views here.


class Home(DataMixin ,ListView):
    model = Product
    # success_url = reverse_lazy("home")
    template_name = "store/home.html"
    context_object_name = 'all_products'

    def get_queryset(self):

        return Product.objects.all()


    def get_context_data(self, *args, **kwargs):

        # Cart.objects.filter(owner=self.request.user).delete()

        context = super().get_context_data(**kwargs)  # like dynamic list
        c_def = self.get_user_context(
            title="Home",
            all_products_like=get_dict_all_products_like(self.request.user))
        return dict(list(context.items()) + list(c_def.items()))



def get_all_product_details(request, slug_id):

    liked = check_if_post_like_and_get_count(slug_id, request.user)

    content = {
        "product": get_special_product(slug_id),
        "image": get_all_aditional_image_by_slug_id(slug_id),
        # "aditional_products": get_list_of_special(get_special_product(slug_id)),
        "header_menu": get_header_menu(),
        "special_menu_function": "All about the product",
        "special_dict_menu": get_dict_aditional_like(request.user, get_list_of_special(get_special_product(slug_id))),
        "is_liked": liked
    }

    return render(request, "store/get_more.html", context=content)


def get_product_featuress(request, slug_id):
    content = {
        "product": get_special_product(slug_id),
    }
    return render(request, "store/get_product_featuress.html", context=content)


def get_product_reviews(request, slug_id):
    content = {
        "product": get_special_product(slug_id),
    }
    return render(request, "store/get_product_reviews.html", context=content)


def get_product_video(request, slug_id):

    content = {
        "product": get_special_product(slug_id),
    }
    return render(request, "store/get_product_video.html", context=content)


def get_product_photo(request, slug_id):

    content = {
        "product": get_special_product(slug_id),
        "images": get_all_aditional_image_by_slug_id(slug_id)
    }
    return render(request, "store/get_product_photo.html", context=content)


def likeView(request, product_id, post_id):
    """ function for adding like to our product """

    response = HttpResponseRedirect(
        get_path_to_redirect(product_id))
    # set_cookies_for_product_like(response, request.user, post_id)
    return press_like_to_product(request, response, post_id)


def get_cart(request):

    user = request.user
    cart = get_cart_by_user(user)
    context = {
        "cart" : cart ,
        "products" : cart.products.all() 
    }
    return render(request, "market/cart.html", context=context)


def add_to_cart(request, product_slug):
    
    user = request.user

    cart = get_cart_by_user(user)
    product = get_special_product(product_slug)

    cart_product = create_cart_product(user, cart, product)
    add_productcart_to_cart(user, cart, cart_product, product)

    return HttpResponseRedirect(reverse("get_cart"))


def remove_from_cart(request, product_slug):
    
    user = request.user

    cart = get_cart_by_user(user)
    product = get_special_product(product_slug)

    cart_product = get_cart_product(user = user, product = product)
    remove_product_from_cart(cart, cart_product, user,product)

    return HttpResponseRedirect(reverse("get_cart"))