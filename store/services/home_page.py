from store.models import Product


def get_all_product():
    result = Product.objects.all()
    return result