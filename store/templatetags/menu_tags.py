from characteristics.services.category_characteristic import get_queryset_for_all_characteristic
from characteristics.models import ProductType
from store.services.get_details import get_header_menu
from django import template
from django.db.models import Count, F, Value
from django.db.models import Q


register = template.Library()

@register.inclusion_tag("store/custom_temp/details_header_menu.html")
def get_read_header_menu(product, special_element):
		
	return {"header_menu":get_header_menu(),
			"product": product,
			"special_element": special_element}	

@register.simple_tag()
def multiply(a, b, *args, **kwargs):
    # you would need to do any localization of the result here
    return a * (100 - b) // 100 if b else a 


@register.inclusion_tag("store/custom_temp/categories_list.html")
def get_categories_list():
	
	categories = ProductType.objects.annotate(publ = F("product__is_available"), cnt = Count("product", filter = Q(publ__gt = 0))).filter(cnt__gt = 0)	
	
	return {"categories":categories}


@register.inclusion_tag("store/custom_temp/characterstics_query.html")
def get_characteristic_query(characteristic):
	
	return {"characteristic":characteristic}

@register.simple_tag()
def replace_word(word, first, second):
    # you would need to do any localization of the result here
    return word.replace(first, second).title()


@register.inclusion_tag("store/custom_temp/category_characterstics_query.html")
def get_characteristic_query_category(query, word):

	result = {
		"queryset" : query.get(word),
		"word": word
	}

	return result