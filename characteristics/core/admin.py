from django.contrib import admin
from django.utils.safestring import mark_safe


class BaseAdmin(admin.ModelAdmin):
    list_per_page = 200  # max post per page
    list_max_show_all = 50  # max posts after clicking on hyperref
    view_on_site = True
    empty_value_display = ""  # empty one of values

    save_on_top = True


class ImageBaseAdmin:
    def get_icon(self, obj):
        if obj.icon:
            return mark_safe(f"<img width=50 src='{obj.icon.url}'>")

    def get_flag(self, obj):
        if obj.flag:
            return mark_safe(f"<img src='{obj.flag.url}'width=40px>")
