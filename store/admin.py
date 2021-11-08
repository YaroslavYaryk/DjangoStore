from django.contrib import admin
from django.utils.safestring import mark_safe
from characteristics.admin import BaseAdmin
from store.models import Characteristics, Coupon, Product, ProductImage, ProductLike, UserCoupon
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget 



class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
    extra = 0
    show_change_link = True


class ProductAdminForm(forms.ModelForm):

    """ Visual redactor depicter """

    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Product
        fields = '__all__'
        # skin = 'moono-dark';


class ProductAdmin(BaseAdmin):

    form = ProductAdminForm
    list_display = ( "name", "type_of_product", "brand", "short_description", 
                    "type_of_product", "get_flag","is_published", "is_available")  # that's will be displayed in django-admin
    list_display_links = ( "name",)  # this ones we can click like links
    search_fields = ("name", "short_description")
    list_editable = ["is_published"]
    inlines = [ProductImageAdmin]
    prepopulated_fields = {"slug": ("name",)}
    # prepopulated_fields = {"slug": ("name",)}
    fields = ( "name", "only_name","slug", "type_of_product", "brand",  "short_description", "description",
                    "photo","video", "is_published",  "country_made", \
                        ("country_brand", "get_flag"), "warranty", "price", "is_available")
    readonly_fields = ("updation_date", "creation_date", "get_flag")

    def get_flag(self, obj):
        if obj.country_brand.flag:
            return mark_safe(f"<img src='{obj.country_brand.flag.url}'width=40px>")    

    get_flag.short_description = "flag"

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


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ( "product" ,'images',)
    list_display_links = ("product", 'images',)
    fields = ('images',)

@admin.register(ProductLike)
class ProductLikeAdmin(admin.ModelAdmin):
    list_display = ( "post" ,'user',)
    list_display_links = ("post", 'user',)
    fields = ( "post" ,'user',)
    readonly_fields = ("post" ,'user',)

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ( "coupon_code" ,'discount',)
    fields = ( "coupon_code" ,'discount',)

@admin.register(UserCoupon)
class UserCouponAdmin(admin.ModelAdmin):
    list_display = ( "ip" ,'coupon',)
    fields = ( "ip" ,'coupon',)

admin.site.register(Product, ProductAdmin)  # in order to show it in django-admin
admin.site.register(Characteristics, CharacteristicAdmin)