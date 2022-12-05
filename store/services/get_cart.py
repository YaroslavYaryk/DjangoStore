from django.contrib.contenttypes.models import ContentType
from store.forms import CouponForm
from store.models import Cart, CartProduct, Coupon, UserCoupon
from django.contrib.admin.options import get_content_type_for_model


def get_cart_by_request_user(user):
    result = Cart.objects.filter(user=user)
    if result:
        return result.first()
    return Cart.objects.create(user=user)


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
    return CartProduct.objects.filter(
        user=user, content_type=type_content, object_id=product.pk
    )


def add_productcart_to_cart(user, cart, cart_product, product):

    type_content = get_content_type_for_model(product)
    existing_cart = cart.products.filter(
        user=user, content_type=type_content, object_id=product.pk
    ).first()
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


def remove_product_from_cart(cart, cart_product, user, product, one_product=False):

    if one_product:
        type_content = get_content_type_for_model(product)
        existing_cart = cart.products.filter(
            user=user, content_type=type_content, object_id=product.pk
        ).first()
        if cart_product:
            cart.products.remove(cart_product[0])
            cart.total_price -= cart_product[0].total_price
        existing_cart.quantity -= 1
        existing_cart.save()
        if existing_cart.quantity < 1:
            cart.total_products -= 1
            remove_cart_product(user, product)
    else:
        for elem in cart_product:
            cart.products.remove(elem)
            cart.total_price -= elem.total_price
        cart.total_products -= 1
        remove_cart_product(user, product)
    cart.save()


def remove_all_from_cart(user):

    Cart.objects.filter(owner=user).delete()
    CartProduct.objects.filter(user=user).delete()


def remove_all_from_cart_api(user):

    Cart.objects.filter(user=user).delete()
    CartProduct.objects.filter(user=user).delete()


def get_check_coupon(request, ip, cart):

    if cart:
        discount = 0
        if request.method == "POST":
            # create a form instance and populate it with data from the request:
            form = CouponForm(request.POST)
            # check  it's valid:
            if form.is_valid():
                coupon = form.cleaned_data["coupon"]
                coupon_queryset = Coupon.objects.filter(coupon_code=coupon)
                if coupon_queryset:
                    discount = coupon_queryset.first().discount
                    UserCoupon.objects.update_or_create(
                        ip=ip, coupon=coupon_queryset.first()
                    )

        # if a GET (or any other method) we'll create a blank form
        else:
            form = CouponForm()
            usr_coupon = [
                elem
                for elem in sorted(
                    UserCoupon.objects.filter(ip=ip), key=lambda x: x.coupon.discount
                )
            ]
            if usr_coupon:
                discount = Coupon.objects.get(
                    coupon_code=usr_coupon[-1].coupon.coupon_code
                ).discount

        cart_button = True
        if not cart.total_products:
            cart_button = False

        return form, discount, cart_button
    return None, None, None


def get_cart_products(cart):

    if cart:
        return cart.products.all()
