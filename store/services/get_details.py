from django.db.models import Q
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls.base import reverse
from characteristics.models import DataStorageDevices, MemoryCapacity, MemorySlot, MemoryType, \
    OperationSystem, ProcessorType, ScreenDiagonal, ScreenFrequency, ScreenType, VideoCard, VideoCardMemory
from characteristics.services.post_characteristic import get_characteristic_by_diagonal_screen, get_characteristic_by_hard_drive, \
    get_characteristic_by_memory_capacity, get_characteristic_by_memory_slots, get_characteristic_by_memory_type, \
    get_characteristic_by_operation_system, get_characteristic_by_processor, \
    get_characteristic_by_screen_frequency, get_characteristic_by_screen_type, get_characteristic_by_video_card, get_characteristic_by_video_card_memory, get_characteristic_field
from store.models import Characteristics, LikedComment, Product, ProductComment, ProductImage, ProductLike
from django.http import Http404
from django.contrib import messages
from django.utils.text import slugify


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

    product_character = Characteristics.objects.filter(
        product__name=product_obj.name).first()

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
    return list_result[:4]


def get_dict_aditional_like(user, list_similar):
    if user.is_authenticated:
        return {prod: ProductLike.objects.filter(user=user, post=prod) for prod in list_similar}
    return {prod: "" for prod in list_similar}


def get_header_menu():

    return {
        "All about the product": "read_more_about_all",
        "Features": "read_features",
        "Reviews": 'read_reviews',
        "Video": "read_video",
        "Photo": "read_photo"
    }

def press_like_to_product(request, response, product_id):

    user = request.user
    try:
        product = Product.objects.get(slug = product_id)
        like = ProductLike.objects.filter(user=user, post=product)

        if like:
            like.delete()  # thre is like put
        else:
            ProductLike.objects.create(
                user=user, post=product)  # create like
    except TypeError:  # is not signed in
        return HttpResponseRedirect(reverse('sign_in'))

    return response


def press_like_to_comment(request, response, comment_pk):

    user = request.user
    try:
        comment = ProductComment.objects.get(pk=comment_pk)
        like = LikedComment.objects.filter(user=user, post_comment=comment)

        if like:
            like.delete()  # thre is like put
        else:
            LikedComment.objects.create(
                user=user, post_comment=comment)  # create like
    except TypeError:  # is not signed in
        return HttpResponseRedirect(reverse('sign_in'))

    return response


def set_cookies_for_product_like(response, user, post_id):

    product = get_special_product(post_id)
    like = ProductLike.objects.filter(user=user, post=product)
    response.set_cookie(product.only_name.replace(" ", "_").strip('"'), "like.com") if like else response.set_cookie(
        product.only_name.replace(" ", "_").strip('"'), "dislike.com")


def check_if_post_like_and_get_count(slug_id, user):

    liked = 0
    if user != "AnonymousUser":
        try:
            liked = ProductLike.objects.filter(user=user, post=Product.objects.
                                               get(slug=slug_id))
            # get like if its liked
        except TypeError:
            pass
    else:
        liked = 0

    return liked


def get_characteristic_by_product(product):

    return Characteristics.objects.get(product=product)


def get_characteristic_query_according_to_character_field(charact_slug, user, charact, get_queryset=False, order_query=False):
    """ accorfing to type of characteristic return correct queryser
        of products with this characteristic """

    if charact == "diagonal_screen":
        return get_characteristic_by_diagonal_screen(user,  get_characteristic_field(charact_slug, ScreenDiagonal), get_queryset, order_query)
    elif charact == "screen_type":
        return get_characteristic_by_screen_type(user,  get_characteristic_field(charact_slug, ScreenType), get_queryset, order_query)
    elif charact == "screen_frequency":
        return get_characteristic_by_screen_frequency(user,  get_characteristic_field(charact_slug, ScreenFrequency), get_queryset, order_query)
    elif charact == "processor_name":
        return get_characteristic_by_processor(user,  get_characteristic_field(charact_slug, ProcessorType), get_queryset, order_query)
    elif charact == "operation_system":
        return get_characteristic_by_operation_system(user,  get_characteristic_field(charact_slug, OperationSystem), get_queryset, order_query)
    elif charact == "memory_capacity":
        return get_characteristic_by_memory_capacity(user,  get_characteristic_field(charact_slug, MemoryCapacity), get_queryset, order_query)
    elif charact == "memory_slots":
        return get_characteristic_by_memory_slots(user, get_characteristic_field(charact_slug, MemorySlot), get_queryset, order_query)
    elif charact == "memory_type":
        return get_characteristic_by_memory_type(user, get_characteristic_field(charact_slug, MemoryType), get_queryset, order_query)
    elif charact == "data_storage":
        return get_characteristic_by_hard_drive(user, get_characteristic_field(charact_slug, DataStorageDevices), get_queryset, order_query)
    elif charact == "video_card":
        return get_characteristic_by_video_card(user, get_characteristic_field(charact_slug, VideoCard), get_queryset, order_query)
    elif charact == "video_card_memory":
        return get_characteristic_by_video_card_memory(user, get_characteristic_field(charact_slug, VideoCardMemory), get_queryset, order_query)


def get_dict_all_comments_like(user, product_id):

    a = {comm: LikedComment.objects.filter(user=user, post_comment=comm) 
            for comm in ProductComment.objects.filter(product=get_special_product(slugify(product_id)))}
    
    print(f"{product_id}")
    print(f"result = {a}")

    if user.is_authenticated:
        return {comm: LikedComment.objects.filter(user=user, post_comment=comm) 
            for comm in ProductComment.objects.filter(product=get_special_product(slugify(product_id)))}
    return {comm: "" for comm in ProductComment.objects.filter(product=get_special_product(slugify(product_id)))}
