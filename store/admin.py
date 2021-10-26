from django.contrib import admin

from store.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):

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
    list_per_page = 200 #max post per page
    list_max_show_all = 50 #max posts after clicking on hyperref
    view_on_site = True
    empty_value_display = 'unknown' #empty one of values

    # inlines = [WomanImageInline] #lwt us add a couple of photos to each post   

    save_on_top = True


admin.site.register(Product, ProductAdmin)  # in order to show it in django-admin
