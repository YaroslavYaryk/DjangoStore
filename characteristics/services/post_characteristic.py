from store.models import Characteristics, ProductLike


def get_characteristic_field(charact_slug, characteristic):
    
    return characteristic.objects.get(slug=charact_slug)


def get_categories_query_according_to_user(user, queryset):
    """ according to anonymous user or not get product
        queryset with liked post by user """

    if user.is_authenticated:
        return {prod.product: ProductLike.objects.filter(user=user, post=prod.product) for prod in queryset}
    return {prod.product: "" for prod in queryset}


def get_characteristic_by_diagonal_screen( user,  characteristic_field, get_queryset=False):
    """ returns generated characteristic query there
        all products with <charact_slug> diagonal screen"""

    queryset = Characteristics.objects.filter(diagonal_screen=characteristic_field)
    if get_queryset:
        return queryset
    return get_categories_query_according_to_user(user, queryset), characteristic_field


def get_characteristic_by_screen_type(user,  characteristic_field, get_queryset=False):
    """ returns generated characteristic query there
        all products with <charact_slug> screen type"""

    queryset = Characteristics.objects.filter(screen_type=characteristic_field)
    if get_queryset:
        return queryset
    return get_categories_query_according_to_user(user, queryset), characteristic_field


def get_characteristic_by_screen_frequency(user,  characteristic_field, get_queryset=False):
    """ returns generated characteristic query there
        all products with <charact_slug> screen type"""

    queryset = Characteristics.objects.filter(screen_frequency=characteristic_field)
    if get_queryset:
        return queryset
    return get_categories_query_according_to_user(user, queryset), characteristic_field


def get_characteristic_by_processor(user,  characteristic_field, get_queryset=False):
    """ returns generated characteristic query there
        all products with <charact_slug> screen type"""

    queryset = Characteristics.objects.filter(processor_name=characteristic_field)
    if get_queryset:
        return queryset
    return get_categories_query_according_to_user(user, queryset), characteristic_field

def get_characteristic_by_operation_system(user,  characteristic_field, get_queryset=False):
    """ returns generated characteristic query there
        all products with <charact_slug> screen type"""

    queryset = Characteristics.objects.filter(operation_system=characteristic_field)
    if get_queryset:
        return queryset
    return get_categories_query_according_to_user(user, queryset), characteristic_field


def get_characteristic_by_memory_capacity(user,  characteristic_field, get_queryset=False):
    """ returns generated characteristic query there
        all products with <charact_slug> screen type"""

    queryset = Characteristics.objects.filter(memory_capacity=characteristic_field)
    if get_queryset:
        return queryset
    return get_categories_query_according_to_user(user, queryset), characteristic_field


def get_characteristic_by_memory_slots(user,  characteristic_field, get_queryset=False):
    """ returns generated characteristic query there
        all products with <charact_slug> screen type"""

    queryset = Characteristics.objects.filter(memory_slots=characteristic_field)
    if get_queryset:
        return queryset
    return get_categories_query_according_to_user(user, queryset), characteristic_field


def get_characteristic_by_memory_type(user,  characteristic_field, get_queryset=False):
    """ returns generated characteristic query there
        all products with <charact_slug> screen type"""

    queryset = Characteristics.objects.filter(memory_type=characteristic_field)
    if get_queryset:
        return queryset
    return get_categories_query_according_to_user(user, queryset), characteristic_field


def get_characteristic_by_hard_drive(user,  characteristic_field, get_queryset=False):
    """ returns generated characteristic query there
        all products with <charact_slug> screen type"""

    queryset = Characteristics.objects.filter(data_storage=characteristic_field)
    if get_queryset:
        return queryset
    return get_categories_query_according_to_user(user, queryset), characteristic_field


def get_characteristic_by_video_card(user,  characteristic_field, get_queryset=False):
    """ returns generated characteristic query there
        all products with <charact_slug> screen type"""

    queryset = Characteristics.objects.filter(video_card=characteristic_field)
    if get_queryset:
        return queryset
    return get_categories_query_according_to_user(user, queryset), characteristic_field


def get_characteristic_by_video_card_memory(user,  characteristic_field, get_queryset=False):
    """ returns generated characteristic query there
        all products with <charact_slug> screen type"""

    queryset = Characteristics.objects.filter(video_card_memory=characteristic_field)
    if get_queryset:
        return queryset
    return get_categories_query_according_to_user(user, queryset), characteristic_field