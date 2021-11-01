from django.contrib.contenttypes.models import ContentType
from store.models import Cart, CartProduct
from django.contrib.admin.options import get_content_type_for_model

def get_cart_by_user(user):

    result = Cart.objects.filter(owner=user, in_order=False)
    if result:
        return result.first()
    return Cart.objects.create(owner=user)


def create_cart_product(user, cart, product):

    cart_product = CartProduct.objects.create(
        user=user, cart=cart, content_object=product
    )
    cart_product.total_price += product.price
    cart_product.save()
    return cart_product


def get_cart_product(user, product):
    
    type_content = get_content_type_for_model(product)
    return CartProduct.objects.filter(user = user, content_type = type_content, object_id=product.pk)

def add_productcart_to_cart(user, cart, cart_product, product):

    # Cart.objects.all().delete()
    # CartProduct.objects.all().delete()

    type_content = get_content_type_for_model(product)
    existing_cart = cart.products.filter(user = user, content_type = type_content, object_id=product.pk).first()
    print(existing_cart)
    if not existing_cart:
        cart.products.add(cart_product)
        cart.total_products += 1
    else:
        existing_cart.quantity += 1
        existing_cart.save()          

    cart.total_price += cart_product.content_object.price 
    cart.save()

def remove_cart_product(user, product):

    get_cart_product(user, product).delete()
    

def remove_product_from_cart(cart, cart_product, user, product):

    for elem in cart_product:
        print(elem)
        cart.products.remove(elem)
        cart.total_price -= elem.total_price
    remove_cart_product(user, product)
    cart.total_products -= 1
    cart.save()
    