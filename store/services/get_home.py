from django.urls.base import reverse
from store.models import Characteristics, Product, ProductImage, ProductLike


def get_dict_all_products_like(user):

    return {prod: ProductLike.objects.filter(user=user, post=prod) for prod in Product.objects.all()}


def get_path_to_redirect(path_to_redirect):
    """ return path to redirect according to page
    where we put like """

    if path_to_redirect == "home":
        return reverse('home')
    return reverse("read_more_about_all", args=[str(path_to_redirect)])
