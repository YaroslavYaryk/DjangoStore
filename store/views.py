from django.shortcuts import render
from store.services.get_details import get_all_aditional_image_by_slug_id, get_special_product

from store.services.home_page import get_all_product

# Create your views here.

def start_page(request):

	storage = {
		"all_products" : get_all_product(),
		"first_product": get_all_product().first()
	}

	return render(request, "store/home.html", context=storage)



def get_product_details(request, slug_id):

	content = {
		"product" : get_special_product(slug_id),
		"image" : get_all_aditional_image_by_slug_id(slug_id),
	}

	return render(request, "store/get_more.html", context=content)