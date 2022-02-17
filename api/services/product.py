from store.models import Product, ProductComment, Coupon


def get_product_by_pk(pk):
    return Product.objects.get(pk=pk)


def get_comment_by_pk(pk):
    return ProductComment.objects.get(pk=pk)


def get_coupon_by_pk(pk):
    return Coupon.objects.get(pk=pk)
