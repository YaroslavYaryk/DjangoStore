from django.contrib import admin
from characteristics.core.admin import BaseAdmin, ImageBaseAdmin
from characteristics.models import\
     CountryBrand, CountryMade, DataStorageDevices, MemoryCapacity, MemorySlot,\
     MemoryType, OperationSystem, ProcessorType, ProductBrand, ProductType,  \
        ScreenDiagonal, ScreenFrequency, \
        ScreenType, VideoCard, VideoCardMemory
from django.utils.safestring import mark_safe        



class ProductBrandAdmin(BaseAdmin):
    """ admin class of each screen diagonal """

    list_display = ("name",)  # that's will be displayed in django-admin
    fields = ( "name", "slug", "description")
    prepopulated_fields = {"slug": ("name",)}


class ScreenDiagonalAdmin(BaseAdmin):
    """ admin class of each screen diagonal """

    list_display = ("name",)  # that's will be displayed in django-admin
    fields = ( "name", "slug")
    prepopulated_fields = {"slug": ("name",)}


class ScreenTypeAdmin(BaseAdmin):
    """ admin class of each screen type """

    list_display = ("name",)  # that's will be displayed in django-admin
    fields = ( "name", "slug", "description")
    prepopulated_fields = {"slug": ("name",)}


class ScreenFrequencyAdmin(BaseAdmin):
    """ admin class of each screen frequency """

    list_display = ("frequency_number",)  # that's will be displayed in django-admin
    fields = ( "frequency_number", "slug")
    prepopulated_fields = {"slug": ("frequency_number",)}


class ProcessorTypeAdmin(BaseAdmin):
    """ admin class of each processor type """

    list_display = ("name",)  # that's will be displayed in django-admin
    fields = ( "name", "slug", "description")
    prepopulated_fields = {"slug": ("name",)}


class OperationSystemAdmin(BaseAdmin):
    """ admin class of each operation system """

    list_display = ("name",)  # that's will be displayed in django-admin
    fields = ( "name", "slug","description")
    prepopulated_fields = {"slug": ("name",)}


class MemoryCapacityAdmin(BaseAdmin):
    """ admin class of each number memory capacity """

    list_display = ("number_of_gigabite",)  # that's will be displayed in django-admin
    fields = ( "number_of_gigabite", "slug")
    prepopulated_fields = {"slug": ("number_of_gigabite",)}


class MemorySlotAdmin(BaseAdmin):
    """ admin class of each number of memory slot """

    list_display = ("number_of_slots",)  # that's will be displayed in django-admin
    fields = ( "number_of_slots", "slug")
    prepopulated_fields = {"slug": ("number_of_slots",)}


class MemoryTypeAdmin(BaseAdmin):
    """ admin class of each type of memory """

    list_display = ("name",)  # that's will be displayed in django-admin
    fields = ( "name", "slug")
    prepopulated_fields = {"slug": ("name",)}


class DataStorageDevicesAdmin(BaseAdmin):
    """ admin class of each data storage (hard drive) """

    list_display = ("hard_drive_capacity", "hard_drive_type")  # that's will be displayed in django-admin
    fields = ( "hard_drive_capacity", "hard_drive_type", "slug")
    prepopulated_fields = {"slug": ("hard_drive_capacity", "hard_drive_type",)}


class VideoCardAdmin(BaseAdmin):
    """ admin class of each video card """

    list_display = ("video_card",)  # that's will be displayed in django-admin
    fields = ( "video_card",  "description", "slug")
    prepopulated_fields = {"slug": ("video_card",)}


class VideoCardMemoryAdmin(BaseAdmin):
    """ admin class of each video card capacity """

    list_display = ("video_card_capacity",)  # that's will be displayed in django-admin
    fields = ( "video_card_capacity", "slug")
    prepopulated_fields = {"slug": ("video_card_capacity",)}


class CountryMadeAdmin(BaseAdmin, ImageBaseAdmin):
    """ admin class of each country where product was made """

    list_display = ("name", "get_flag")  # that's will be displayed in django-admin
    fields = ( "name", "flag","slug")
    prepopulated_fields = {"slug": ("name",)}

    ImageBaseAdmin.get_flag.short_description = "flag"




class CountryBrandAdmin(BaseAdmin, ImageBaseAdmin):
    """ admin class of each country where brand was founded """

    list_display = ("name", "get_flag")  # that's will be displayed in django-admin
    fields = ( "name", "flag","slug")
    prepopulated_fields = {"slug": ("name",)}

    ImageBaseAdmin.get_flag.short_description = "flag"


class ProductTypeAdmin(BaseAdmin, ImageBaseAdmin):
    """ admin class of each product type(laptop, computer) """

    list_display = ("name", "get_icon")  # that's will be displayed in django-admin
    fields = ( "name", "description","slug", "icon")
    prepopulated_fields = {"slug": ("name",)}

    ImageBaseAdmin.get_icon.short_description = "icon"

admin.site.register(ProductBrand, ProductBrandAdmin)
admin.site.register(ScreenDiagonal, ScreenDiagonalAdmin)  # in order to show it in django-admin
admin.site.register(ScreenType, ScreenTypeAdmin)
admin.site.register(ScreenFrequency, ScreenFrequencyAdmin)
admin.site.register(ProcessorType, ProcessorTypeAdmin)
admin.site.register(OperationSystem, OperationSystemAdmin)
admin.site.register(MemoryCapacity, MemoryCapacityAdmin)
admin.site.register(MemorySlot, MemorySlotAdmin)
admin.site.register(MemoryType, MemoryTypeAdmin)
admin.site.register(DataStorageDevices, DataStorageDevicesAdmin)
admin.site.register(VideoCard, VideoCardAdmin)
admin.site.register(VideoCardMemory, VideoCardMemoryAdmin)
admin.site.register(CountryBrand, CountryBrandAdmin)
admin.site.register(CountryMade, CountryMadeAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
