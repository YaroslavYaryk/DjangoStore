from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from store.services.get_category import add_view_of_post
from store.forms import LoginUserForm, RegisterUserForm
from characteristics.services.category_characteristic import get_queryset_for_all_characteristic
from store.utils import DataMixin
from store.services.get_cart import add_productcart_to_cart, create_cart_product, \
    get_cart_by_user, get_cart_product, get_cart_products, get_check_coupon, \
        remove_all_from_cart, remove_product_from_cart
from store.services.get_home import get_dict_all_products_like, get_dict_query_products_like, get_input_search_query, get_path_to_redirect
from store.models import Product
from store.services.get_details import check_if_post_like_and_get_count, \
    get_all_aditional_image_by_slug_id, \
        get_characteristic_by_product, get_dict_aditional_like, \
    get_header_menu, get_list_of_special, get_special_product, press_like_to_product
from django.contrib.auth.views import LoginView, LogoutView

from loguru import logger as log


log.add("/home/yaroslav/Programming/Python/Django/StoreProject/market/logging/log2.log",
        enqueue=True, level="DEBUG", rotation="10 MB")


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
            order = "newest",
            place="home",
            title="Home",
            all_products_like=get_dict_all_products_like(self.request.user))
        return dict(list(context.items()) + list(c_def.items()))


def get_all_product_details(request, slug_id):

    liked = check_if_post_like_and_get_count(slug_id, request.user)

    add_view_of_post(request, get_special_product(slug_id))
    content = {
        "product": get_special_product(slug_id),
        "image": get_all_aditional_image_by_slug_id(slug_id),
        # "aditional_products": get_list_of_special(get_special_product(slug_id)),
        "header_menu": get_header_menu(),
        "special_menu_function": "All about the product",
        "special_dict_menu": get_dict_aditional_like(request.user, get_list_of_special(get_special_product(slug_id))),
        "is_liked": liked,
        "cart": get_cart_by_user(request.user)
    }

    return render(request, "store/get_more.html", context=content)


def get_product_featuress(request, slug_id):
    content = {
        "product": get_special_product(slug_id),
        "cart": get_cart_by_user(request.user),
        "characteristic": get_characteristic_by_product(get_special_product(slug_id))
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

    
    form, discount, cart_button = get_check_coupon(request, user, cart)

    context = {
        "cart" : cart ,
        "products" : get_cart_products(cart),
        'form': form,
        "discount" : discount,
        "cart_button": cart_button,
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

def remove_one_product(request, product_slug):

    user = request.user

    cart = get_cart_by_user(user)
    product = get_special_product(product_slug)

    cart_product = get_cart_product(user = user, product = product)

    remove_product_from_cart(cart, cart_product, user,product, True)
    return HttpResponseRedirect(reverse("get_cart"))

def delete_cart(request):

    user = request.user
    remove_all_from_cart(user)
    return HttpResponseRedirect(reverse("get_cart"))



class Category(DataMixin ,ListView):
    model = Product
    # success_url = reverse_lazy("home")
    template_name = "store/get_categories.html"
    context_object_name = 'products'
    
    def get_queryset(self):

        category_slug = self.kwargs["category_slug"]
        return Product.objects.filter(type_of_product__slug = category_slug)


    def get_context_data(self, *args, **kwargs):

        # Cart.objects.filter(owner=self.request.user).delete()
        category_slug = self.kwargs["category_slug"]
        context = super().get_context_data(**kwargs)  # like dynamic list
        c_def = self.get_user_context(
            category = Product.objects.filter(type_of_product__slug = category_slug).first().type_of_product,
            characteristic_queryset = get_queryset_for_all_characteristic(),
            product_likes = get_dict_query_products_like(self.request.user, category_slug)
        )
        return dict(list(context.items()) + list(c_def.items()))


class SearchProduct(DataMixin ,ListView):
    """ class of search product to work with them """

    model = Product
    # success_url = reverse_lazy("home")
    template_name = "store/search_products.html"
    context_object_name = 'products'

    def get_queryset(self):

        print(get_input_search_query(self.request))
        return Product.objects.filter(name__icontains=get_input_search_query(self.request))

    def get_context_data(self, *args, **kwargs):

        # Cart.objects.filter(owner=self.request.user).delete()
        context = super().get_context_data(**kwargs)  # like dynamic list
        c_def = self.get_user_context(
            title = get_input_search_query(self.request),
            all_products_like=get_dict_all_products_like(self.request.user)
        )
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, SuccessMessageMixin, CreateView):
    """Show register form"""

    form_class = RegisterUserForm
    template_name = 'market/register.html'
    success_url = reverse_lazy("sign_in")
    success_message = "User added successfully"
    error_message = "Registration error"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        c_def = self.get_user_context(
            title="Registration", ico="menu/img/ico/home_pink.png")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, SuccessMessageMixin, LoginView):

    """Autorization class"""

    form_class = LoginUserForm
    template_name = 'market/sign_in.html'
    error_message = "Something went wrong"
    success_url = reverse_lazy("home")
    user = ""
    success_message = f"Successfully sign in"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        c_def = self.get_user_context(
            title="Sign in", ico="menu/img/ico/home_pink.png")

        return dict(list(context.items()) + list(c_def.items()))


class ProfileView(DataMixin, ListView):

    model = User
    template_name = "market/profile.html"

    def get_context_data(self, *args, **kwargs):
        try:
            user = self.request.user
        except:
            user = None    
        context = super().get_context_data(*args, **kwargs)
        c_def = self.get_user_context(
            user = user,
            title="Profile",
            
            )
        return dict(list(context.items()) + list(c_def.items()))

class LogoutUser(LogoutView, SuccessMessageMixin):

    next_page = "home"
    success_message = "Logout successfully"
