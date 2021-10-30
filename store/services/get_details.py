from django.db.models import Q
from django.shortcuts import get_object_or_404
from store.models import Characteristics, Product, ProductImage
from django.http import Http404


def get_special_product(product_id):
    """ get object by slug id """

    # try except logic
    try:
        return get_object_or_404(Product, slug=product_id)
    except Product.DoesNotExist:
        raise Http404("Given query not found....")


def get_all_aditional_image_by_slug_id(slug_id):
    return ProductImage.objects.filter(product__slug=slug_id)


def get_list_of_special(product_obj):

    product_character = Characteristics.objects.get(
        product__name=product_obj.name)

    similar_characteristics = Characteristics.objects.filter((
        Q(processor_name=product_character.processor_name) |
        Q(memory_capacity=product_character.memory_capacity) |
        Q(data_storage=product_character.data_storage))
    )
    list_result = [elem.product for elem in similar_characteristics]
    similar_product_price = Product.objects.filter(
        Q(price__gte=product_obj.price-1000) & Q(price__lte=product_obj.price+1000))
    list_result += [elem for elem in similar_product_price if elem not in list_result]
    list_result.remove(product_obj)
    return list_result[:5]


def get_header_menu():

    return {
        "All about the product": "read_more_about_all",
        "Features" : "read_features",
        "Reviews" : 'read_reviews',
        "Video" : "read_video",
        "Photo" : "read_photo"
    }
