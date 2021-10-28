from django.shortcuts import render

from store.services.home_page import get_all_product

# Create your views here.

def start_page(request):

	storage = {
		"all_products" : get_all_product()
	}

	return render(request, "store/home.html", context=storage)