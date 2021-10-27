from django.contrib import admin
from characteristics.admin import BaseAdmin
from store.models import Characteristics, Product





class ProductAdmin(BaseAdmin):

    list_display = ( "name", "short_description","creation_date", "updation_date",
                    "photo","video", "is_published", "type_of_product", "country_made", \
                        "country_brand", "warranty")  # that's will be displayed in django-admin
    list_display_links = ( "name",)  # this ones we can click like links
    search_fields = ("name", "short_description")
    list_editable = ["is_published"]
    # prepopulated_fields = {"slug": ("name",)}
    fields = ( "name", "short_description", "description",
                    "photo","video", "is_published", "type_of_product", "country_made", \
                        "country_brand", "warranty")
    readonly_fields = ("updation_date", "creation_date",)

class CharacteristicAdmin(BaseAdmin):

    list_display = ( "product", "processor_name", "operation_system",
        "memory_capacity", "memory_type", "color")  # that's will be displayed in django-admin
    list_display_links = ( "product",)  # this ones we can click like links
    search_fields = ("product", "processor_name")
    fields = ("product", "diagonal_screen", "screen_type", "screen_frequency",
         "camera", "processor_name", "operation_system", "memory_capacity", 
         "memory_slots","memory_type", "data_storage", "video_card", "video_card_memory",
         "color", "weight", "battery", "manipulators", "height", "width", "depth",
         "corp_material", "network_adapters", "wireless_connection", "input_output")


admin.site.register(Product, ProductAdmin)  # in order to show it in django-admin
admin.site.register(Characteristics, CharacteristicAdmin)