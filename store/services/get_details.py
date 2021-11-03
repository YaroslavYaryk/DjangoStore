from django.db.models import Q
from django.shortcuts import get_object_or_404
from store.models import Characteristics, Product, ProductImage, ProductLike
from django.http import Http404
from django.contrib import messages


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


def get_dict_aditional_like(user, list_similar):
    if user.is_authenticated:
        return {prod: ProductLike.objects.filter(user=user, post=prod) for prod in list_similar}
    return {prod: "" for prod in list_similar}

def get_header_menu():

    return {
        "All about the product": "read_more_about_all",
        "Features" : "read_features",
        "Reviews" : 'read_reviews',
        "Video" : "read_video",
        "Photo" : "read_photo"
    }


def press_like_to_product(request, response, post_id):

    user = request.user
    try:
        product = Product.objects.get(slug=post_id)  # get post
        like = ProductLike.objects.filter(user=user, post=product)

        if like:
            like.delete()  # thre is like put
        else:
            ProductLike.objects.create(user=user, post=product)  # create like
    except TypeError:  # is not signed in
        messages.add_message(request, messages.WARNING,
                             'to put like you need to sign in first ')
        # reirect to sign in  
        return response

    return  response 


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


def get_characteristic_field(charact_slug, characteristic):

    return characteristic.objects.get(slug = charact_slug)


def get_characteristic_by_field(charact_slug, characteristic, field):

    characteristic_field = get_characteristic_field(charact_slug, characteristic)    

    return Characteristics.objects.filter(diagonal_screen = characteristic_field)