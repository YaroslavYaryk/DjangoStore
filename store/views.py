from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.utils.text import slugify
from django.views.generic import ListView
from store.services.order import get_place
from store.services.get_category import add_view_of_post, get_client_ip
from store.forms import ProductCommentForm
from characteristics.services.category_characteristic import (
    get_queryset_for_all_characteristic,
)
from store.utils import DataMixin
from store.services.get_cart import (
    add_productcart_to_cart,
    create_cart_product,
    get_cart_by_user,
    get_cart_product,
    get_cart_products,
    get_check_coupon,
    remove_all_from_cart,
    remove_product_from_cart,
)
from store.services.get_home import (
    get_dict_all_products_like,
    get_dict_query_products_like,
    get_input_search_query,
    get_order_dict,
    get_path_to_redirect,
)
from store.models import Characteristics, Product, ProductComment
from store.services.get_details import (
    check_if_post_like_and_get_count,
    get_all_aditional_image_by_slug_id,
    get_characteristic_by_product,
    get_dict_aditional_like,
    get_header_menu,
    get_list_of_special,
    get_special_product,
    press_like_to_comment,
    press_like_to_product,
)
from django.views.generic.list import ListView


class Home(DataMixin, ListView):
    model = Product
    # success_url = reverse_lazy("home")
    template_name = "store/home.html"
    context_object_name = "all_products"

    def get_queryset(self):

        choice = self.request.GET.get("order")
        self.choice = get_place(self.request, choice)
        return Product.objects.order_by(get_order_dict()[self.choice])

    def get_context_data(self, *args, **kwargs):

        # Cart.objects.filter(owner=self.request.user).delete()
        context = super().get_context_data(**kwargs)  # like dynamic list
        c_def = self.get_user_context(
            order=self.choice,
            title="Home",
            all_products_like=get_dict_all_products_like(self.request.user),
        )
        return dict(list(context.items()) + list(c_def.items()))


def get_all_product_details(request, slug_id):

    ip = get_client_ip(request)
    liked = check_if_post_like_and_get_count(slug_id, request.user)

    add_view_of_post(request, get_special_product(slug_id))
    content = {
        "product": get_special_product(slug_id),
        "image": get_all_aditional_image_by_slug_id(slug_id),
        "header_menu": get_header_menu(),
        "special_menu_function": "All about the product",
        "special_dict_menu": get_dict_aditional_like(
            request.user, get_list_of_special(get_special_product(slug_id))
        ),
        "is_liked": liked,
        "cart": get_cart_by_user(ip),
    }

    return render(request, "store/get_more.html", context=content)


def get_product_featuress(request, slug_id):
    ip = get_client_ip(request)
    content = {
        "product": get_special_product(slug_id),
        "cart": get_cart_by_user(ip),
        "characteristic": get_characteristic_by_product(get_special_product(slug_id)),
    }
    return render(request, "store/get_product_featuress.html", context=content)


def get_product_reviews(request, slug_id):

    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ProductCommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            comment = form.cleaned_data["comment"]
            # process the data in form.cleaned_data as required
            if request.user.is_authenticated:
                ProductComment.objects.create(
                    product=get_special_product(slug_id),
                    user=request.user,
                    comment=comment,
                )

            else:
                return HttpResponseRedirect(reverse("sign_in"))
            # redirect to a new URL:
            return HttpResponseRedirect(reverse("read_reviews", args=[slug_id]))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProductCommentForm()

    content = {
        "comments": ProductComment.objects.filter(product=get_special_product(slug_id)),
        "product": get_special_product(slug_id),
        "form": form,
        "cart": get_cart_by_user(get_client_ip(request)),
    }
    return render(request, "store/get_product_reviews.html", context=content)


def get_product_video(request, slug_id):

    content = {
        "product": get_special_product(slug_id),
        "cart": get_cart_by_user(get_client_ip(request)),
    }
    return render(request, "store/get_product_video.html", context=content)


def get_product_photo(request, slug_id):

    content = {
        "product": get_special_product(slug_id),
        "images": get_all_aditional_image_by_slug_id(slug_id),
        "cart": get_cart_by_user(get_client_ip(request)),
    }
    return render(request, "store/get_product_photo.html", context=content)


def likeView(request, product_id, post_id, cat):
    """function for adding like to our product"""
    if cat == "0":
        response = HttpResponseRedirect(get_path_to_redirect(product_id))
    elif cat in ["laptop", "phone", "computer"]:
        response = HttpResponseRedirect(
            reverse(product_id, kwargs={"category_slug": cat})
        )
    elif cat == "search":
        response = redirect(reverse("search_products"), get_input_search_query(request))
    else:
        response = HttpResponseRedirect(
            reverse(
                "get_characteristic_query",
                kwargs={"charact": product_id, "charact_slug": cat},
            )
        )
    return press_like_to_product(request, response, post_id)


def get_cart(request):

    ip = get_client_ip(request)
    cart = get_cart_by_user(ip)

    form, discount, cart_button = get_check_coupon(request, ip, cart)

    context = {
        "cart": cart,
        "products": get_cart_products(cart),
        "form": form,
        "discount": discount,
        "cart_button": cart_button,
    }

    return render(request, "market/cart.html", context=context)


def add_to_cart(request, product_slug):

    ip = get_client_ip(request)

    cart = get_cart_by_user(ip)
    product = get_special_product(product_slug)

    cart_product = create_cart_product(ip, cart, product)
    add_productcart_to_cart(ip, cart, cart_product, product)

    return HttpResponseRedirect(reverse("get_cart"))


def remove_from_cart(request, product_slug):

    ip = get_client_ip(request)

    cart = get_cart_by_user(ip)
    product = get_special_product(product_slug)

    cart_product = get_cart_product(user=ip, product=product)
    remove_product_from_cart(cart, cart_product, ip, product)

    return HttpResponseRedirect(reverse("get_cart"))


def remove_one_product(request, product_slug):

    ip = get_client_ip(request)

    cart = get_cart_by_user(ip)
    product = get_special_product(product_slug)

    cart_product = get_cart_product(user=ip, product=product)

    remove_product_from_cart(cart, cart_product, ip, product, True)
    return HttpResponseRedirect(reverse("get_cart"))


def delete_cart(request):

    ip = get_client_ip(request)
    remove_all_from_cart(ip)
    return HttpResponseRedirect(reverse("get_cart"))


class Category(DataMixin, ListView):
    model = Product
    # success_url = reverse_lazy("home")
    template_name = "store/get_categories.html"
    context_object_name = "products"

    def get_queryset(self):

        choice = self.request.GET.get("order")
        self.choice = get_place(self.request, choice)

        category_slug = self.kwargs["category_slug"]
        return Product.objects.filter(
            type_of_product__slug=slugify(category_slug)
        ).order_by(get_order_dict().get(self.choice))

    def get_context_data(self, *args, **kwargs):

        # Cart.objects.filter(owner=self.request.user).delete()
        category_slug = self.kwargs["category_slug"]
        context = super().get_context_data(**kwargs)  # like dynamic list
        c_def = self.get_user_context(
            order=self.choice,
            category=Product.objects.filter(
                type_of_product__slug=slugify(category_slug)
            )
            .first()
            .type_of_product,
            characteristic_queryset=get_queryset_for_all_characteristic(),
            product_likes=get_dict_query_products_like(
                self.request.user, slugify(category_slug)
            ),
        )
        return dict(list(context.items()) + list(c_def.items()))


class SearchProduct(DataMixin, ListView):
    """class of search product to work with them"""

    model = Product
    # success_url = reverse_lazy("home")
    template_name = "store/search_products.html"
    context_object_name = "products"

    def render_to_response(self, context, **response_kwargs):
        response = super(SearchProduct, self).render_to_response(
            context, **response_kwargs
        )
        response.set_cookie(get_input_search_query(self.request), "search")
        return response

    def get_queryset(self):

        choice = self.request.GET.get("order")
        self.choice = get_place(self.request, choice)
        return Product.objects.filter(
            name__icontains=get_input_search_query(self.request)
        ).order_by(get_order_dict().get(self.choice))

    def get_context_data(self, *args, **kwargs):

        # Cart.objects.filter(owner=self.request.user).delete()
        context = super().get_context_data(**kwargs)  # like dynamic list
        c_def = self.get_user_context(
            order=self.choice,
            title=get_input_search_query(self.request),
            all_products_like=get_dict_all_products_like(self.request.user),
        )
        return dict(list(context.items()) + list(c_def.items()))


def likeCommentView(request, product_id, comment_pk):
    """function for adding like to our product"""

    response = HttpResponseRedirect(
        reverse("read_reviews", kwargs={"slug_id": product_id})
    )
    # set_cookies_for_product_like(response, request.user, post_id)
    return press_like_to_comment(request, response, comment_pk)


def handle_not_found(request, exception):
    return render(request, "admin/404.html")


def handle_server_error(request):
    return render(request, "admin/500.html")


def handler_forbiden(request, exception):
    return render(request, "admin/403.html")


def handle_url_error(request, exception):
    return render(request, "admin/400.html", status=400)


def get_information_about(request):

    ip = get_client_ip(request)
    context = {
        "cart": get_cart_by_user(ip),
    }

    return render(request, "market/about.html", context=context)
