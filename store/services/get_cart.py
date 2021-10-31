from store.models import Cart, CartProduct
from pprint import pprint

def get_cart_by_user(user):
    
    result = Cart.objects.filter(owner=user, in_order=True)
    if result:
        return result.first()
    return Cart.objects.create(owner=user)

def create_cart_product(user, cart, product):

    # result = CartProduct.objects.filter(user=user, cart=get_cart_by_user(user), product=product)
    # if not result:
    #     return CartProduct.objects.create(
    #         user=user, cart=get_cart_by_user(user), product=product
    #     )
    pass


def add_productcart_to_product(cart, cart_product):

    pprint(cart.products.all())
    if cart_product not in cart.products.all():
        cart.products.add(cart_product) 