from store.models import Product, ProductComment, Coupon
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
