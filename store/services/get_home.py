from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls.base import reverse
from store.services.get_category import get_client_ip
from store.models import  Product, ProductLike, UserSearchHistory
from django.core.mail import send_mail, BadHeaderError, EmailMessage, EmailMultiAlternatives


def get_dict_all_products_like(user):
    if user.is_authenticated:
        return {prod: ProductLike.objects.filter(user=user, post=prod) for prod in Product.objects.all()}
    return {prod:"" for prod in Product.objects.all()}

def get_dict_query_products_like(user, category_slug):
    if user.is_authenticated:
        return {prod: ProductLike.objects.filter(user=user, post=prod) for prod in  Product.objects.filter(type_of_product__slug = category_slug)}
    return {prod:"" for prod in Product.objects.all()}



def get_path_to_redirect(path_to_redirect):
    """ return path to redirect according to page
    where we put like """

    if path_to_redirect == "home":
        return reverse('home')
    return reverse("read_more_about_all", args=[str(path_to_redirect)])


def get_input_search_query(request):

    ip = get_client_ip(request)
    search_query = request.GET.get("search_query")

    if search_query:
        UserSearchHistory.objects.create(ip = ip, search_value = search_query)
    else:
        search_query = UserSearchHistory.objects.filter(ip = ip).last().search_value

    return search_query    


def get_order_dict():

    return  {
            "newest": "-creation_date", 
            "most popular 👇": "-ip",
            "most popular 👆": "ip",
            "price 👆": "price",
            "price 👇": "-price"
            }    

def get_order_dict2():

    return  {
            "newest": "-product__creation_date", 
            "most popular 👇": "-product__ip",
            "most popular 👆": "product__ip",
            "price 👆": "product__price",
            "price 👇": "-product__price"
            }             


def send_mail_register(request):

    user = User.objects.order_by("-id").first() #get last registered
    message = "Thanks for taking our site, i'm really delightful that you're here, keep on developing, you've got this"
    user.email_user('Welcome', message , fail_silently=True)

    return HttpResponseRedirect(reverse("sign_in"))           