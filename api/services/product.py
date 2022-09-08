from store.models import Characteristics, LikedComment, Product, ProductComment, Coupon
from decouple import config


def get_product_by_pk(pk):
    return Product.objects.get(pk=pk)


def get_comment_by_pk(pk):
    return ProductComment.objects.get(pk=pk)


def get_coupon_by_pk(pk):
    return Coupon.objects.get(pk=pk)


def get_photos(instance):
    return {
        "photos": [
            {
                "id": el.id,
                "url": f"{config('USERHOST')}:{config('USERPORT')}{el.photo.url}",
            }
            for el in instance.photos.all()
        ]
    }


def get_likesCount(instance):
    return LikedComment.objects.filter(post_comment=instance).count()


def search_queryset(pattern):
    return Product.objects.filter(name__icontains=pattern)


def get_characteristic_queryset(search_queryset):

    return Characteristics.objects.filter(product__in=search_queryset)


def get_filtered_product_queryset(characteristic_queryset, filter_options):
    print([el.processor_name.slug for el in characteristic_queryset])

    query = {
        f"{el['name']}__slug__in": el["value"]
        for el in filter_options
        if el["name"] != "priceBlock"
    }
    new_queryset = characteristic_queryset.filter(**query)

    return Product.objects.filter(id__in=[el.product.id for el in new_queryset])


def get_price_filtered_queryset(queryset, filter_options):
    price = [el for el in filter_options if el["name"] == "priceBlock"]
    if len(price):
        # print(price[0]["value"].split("-"))
        min_price, max_price = map(int, price[0]["value"][0].split("-"))
        return queryset.filter(price__gte=min_price, price__lte=max_price)

    return queryset


def handle_filter_queryset(search_queryset, filter_options):
    characteristic_queryset = get_characteristic_queryset(search_queryset)
    filtered_queryset = get_filtered_product_queryset(
        characteristic_queryset, filter_options
    )
    price_filtered_queryset = get_price_filtered_queryset(
        filtered_queryset, filter_options
    )
    return price_filtered_queryset


def category_queryset(pattern):
    return Product.objects.filter(type_of_product__slug=pattern)


def characteristic_queryset(pattern):
    charact_query = Characteristics.objects.filter(
        **{f"{pattern['name']}__slug": pattern["value"]}
    )
    return Product.objects.filter(id__in=[el.product.id for el in charact_query])
