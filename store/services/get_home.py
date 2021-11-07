from django.urls.base import reverse
from store.models import  Product, ProductLike, UserSearchHistory


def get_dict_all_products_like(user):
    if user.is_authenticated:
        return {prod: ProductLike.objects.filter(user=user, post=prod) for prod in Product.objects.all()}
    return {prod:"" for prod in Product.objects.all()}

def get_dict_query_products_like(user, category_slug):
    if user.is_authenticated:
        return {prod: ProductLike.objects.filter(user=user, post=prod) for prod in  Product.objects.filter(type_of_product__slug = category_slug)}
    return {prod:"" for prod in Product.objects.all()}



def get_path_to_redirect(path_to_redirect):
    """ return path to redirect according to page
    where we put like """

    if path_to_redirect == "home":
        return reverse('home')
    return reverse("read_more_about_all", args=[str(path_to_redirect)])


def get_input_search_query(request):

    search_query = request.GET.get("search_query")

    if search_query and request.user.is_authenticated:
        UserSearchHistory.objects.create(user = request.user, search_value = search_query)
    else:
        search_query = UserSearchHistory.objects.all().last().search_value

    return search_query    