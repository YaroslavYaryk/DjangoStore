from store.services.get_details import get_header_menu
from django import template


register = template.Library()

@register.inclusion_tag("store/custom_temp/details_header_menu.html")
def get_read_header_menu(product, special_element):
		
	return {"header_menu":get_header_menu(),
			"product": product,
			"special_element": special_element}	

