from django.shortcuts import get_object_or_404
from store.models import Product, ProductImage
from django.http import Http404


def get_special_product(product_id):
    """ get object by slug id """

     # try except logic
    try:
        return get_object_or_404(Product, slug=product_id)
    except Product.DoesNotExist:
        raise Http404("Given query not found....")


def get_all_aditional_image_by_slug_id(slug_id):
    return ProductImage.objects.filter(product__slug = slug_id)