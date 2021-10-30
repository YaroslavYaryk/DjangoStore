from django.shortcuts import render
from django.views.generic import ListView
from store.models import Product
from store.services.get_details import get_all_aditional_image_by_slug_id, \
    get_header_menu, get_list_of_special, get_special_product


# Create your views here.


class Home(ListView):
    model = Product
    # success_url = reverse_lazy("home")
    template_name = "store/home.html"
    context_object_name = 'all_products'

    def get_queryset(self):

        return Product.objects.all()

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["title"] = "Home"
        return data



def get_all_product_details(request, slug_id):

    content = {
        "product": get_special_product(slug_id),
        "image": get_all_aditional_image_by_slug_id(slug_id),
        "aditional_products": get_list_of_special(get_special_product(slug_id)),
        "header_menu": get_header_menu(),
        "special_menu_function": "All about the product"
    }

    return render(request, "store/get_more.html", context=content)


def get_product_featuress(request, slug_id):
    content = {
        "product": get_special_product(slug_id),
    } 
    return render(request, "store/get_product_featuress.html", context=content)


def get_product_reviews(request, slug_id):
    content = {
        "product": get_special_product(slug_id),
    }   
    return render(request, "store/get_product_reviews.html", context=content)


def get_product_video(request, slug_id):

    content = {
        "product": get_special_product(slug_id),
    }    
    return render(request, "store/get_product_video.html", context=content)


def get_product_photo(request, slug_id):

    content = {
        "product": get_special_product(slug_id),
        "images": get_all_aditional_image_by_slug_id(slug_id)
    }    
    return render(request, "store/get_product_photo.html", context=content)
