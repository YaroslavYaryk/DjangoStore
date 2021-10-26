from django.contrib import admin
from characteristics.models import DataStorageDevices, MemoryCapacity, MemorySlot,\
     MemoryType, OperationSystem, ProcessorType, Screen, \
        ScreenDiagonal, ScreenFrequency, \
        ScreenType, VideoCard, VideoCardMemory



# Register your models here.
class ScreenAdmin(admin.ModelAdmin):
    """ admin class of screen """
    
    list_display = ("diagonal_screen","screen_type", "screen_frequency", "camera")  # that's will be displayed in django-admin
    fields = ( "diagonal_screen", "screen_type", "screen_frequency", "camera")
    list_per_page = 200 #max post per page
    list_max_show_all = 50 #max posts after clicking on hyperref
    view_on_site = True
    empty_value_display = 'unknown' #empty one of values

    save_on_top = True


class ScreenDiagonalAdmin(admin.ModelAdmin):
    """ admin class of each screen diagonal """

    list_display = ("name",)  # that's will be displayed in django-admin
    fields = ( "name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    list_per_page = 200 #max post per page
    list_max_show_all = 50 #max posts after clicking on hyperref
    view_on_site = True
    empty_value_display = 'unknown' #empty one of values

    save_on_top = True


class ScreenTypeAdmin(admin.ModelAdmin):
    """ admin class of each screen type """

    list_display = ("name",)  # that's will be displayed in django-admin
    fields = ( "name", "slug", "description")
    prepopulated_fields = {"slug": ("name",)}
    list_per_page = 200 #max post per page
    list_max_show_all = 50 #max posts after clicking on hyperref
    view_on_site = True
    empty_value_display = 'unknown' #empty one of values

    save_on_top = True


class ScreenFrequencyAdmin(admin.ModelAdmin):
    """ admin class of each screen frequency """

    list_display = ("frequency_number",)  # that's will be displayed in django-admin
    fields = ( "frequency_number", "slug")
    prepopulated_fields = {"slug": ("frequency_number",)}
    list_per_page = 200 #max post per page
    list_max_show_all = 50 #max posts after clicking on hyperref
    view_on_site = True
    empty_value_display = 'unknown' #empty one of values

    save_on_top = True


class ProcessorTypeAdmin(admin.ModelAdmin):
    """ admin class of each processor type """

    list_display = ("name",)  # that's will be displayed in django-admin
    fields = ( "name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    list_per_page = 200 #max post per page
    list_max_show_all = 50 #max posts after clicking on hyperref
    view_on_site = True
    empty_value_display = 'unknown' #empty one of values

    save_on_top = True

class OperationSystemAdmin(admin.ModelAdmin):
    """ admin class of each operation system """

    list_display = ("name",)  # that's will be displayed in django-admin
    fields = ( "name", "slug","description")
    prepopulated_fields = {"slug": ("name",)}
    list_per_page = 200 #max post per page
    list_max_show_all = 50 #max posts after clicking on hyperref
    view_on_site = True
    empty_value_display = 'unknown' #empty one of values

    save_on_top = True    


class MemoryCapacityAdmin(admin.ModelAdmin):
    """ admin class of each number memory capacity """

    list_display = ("number_of_gigabite",)  # that's will be displayed in django-admin
    fields = ( "number_of_gigabite", "slug")
    prepopulated_fields = {"slug": ("number_of_gigabite",)}
    list_per_page = 200 #max post per page
    list_max_show_all = 50 #max posts after clicking on hyperref
    view_on_site = True
    empty_value_display = 'unknown' #empty one of values

    save_on_top = True 


class MemorySlotAdmin(admin.ModelAdmin):
    """ admin class of each number of memory slot """

    list_display = ("number_of_slots",)  # that's will be displayed in django-admin
    fields = ( "number_of_slots", "slug")
    prepopulated_fields = {"slug": ("number_of_slots",)}
    list_per_page = 200 #max post per page
    list_max_show_all = 50 #max posts after clicking on hyperref
    view_on_site = True
    empty_value_display = 'unknown' #empty one of values

    save_on_top = True 


class MemoryTypeAdmin(admin.ModelAdmin):
    """ admin class of each type of memory """

    list_display = ("name",)  # that's will be displayed in django-admin
    fields = ( "name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    list_per_page = 200 #max post per page
    list_max_show_all = 50 #max posts after clicking on hyperref
    view_on_site = True
    empty_value_display = 'unknown' #empty one of values

    save_on_top = True


class DataStorageDevicesAdmin(admin.ModelAdmin):
    """ admin class of each data storage (hard drive) """

    list_display = ("hard_drive_capacity", "hard_drive_type")  # that's will be displayed in django-admin
    fields = ( "hard_drive_capacity", "hard_drive_type", "slug")
    prepopulated_fields = {"slug": ("hard_drive_type",)}
    list_per_page = 200 #max post per page
    list_max_show_all = 50 #max posts after clicking on hyperref
    view_on_site = True
    empty_value_display = 'unknown' #empty one of values

    save_on_top = True


class VideoCardAdmin(admin.ModelAdmin):
    """ admin class of each video card """

    list_display = ("video_card", "videocard_memory",)  # that's will be displayed in django-admin
    fields = ( "video_card"  "videocard_memory", "slug")
    prepopulated_fields = {"slug": ("videocard_memory",)}
    list_per_page = 200 #max post per page
    list_max_show_all = 50 #max posts after clicking on hyperref
    view_on_site = True
    empty_value_display = 'unknown' #empty one of values

    save_on_top = True


class VideoCardMemoryAdmin(admin.ModelAdmin):
    """ admin class of each video card capacity """

    list_display = ("video_card_capacity",)  # that's will be displayed in django-admin
    fields = ( "video_card_capacity", "slug")
    prepopulated_fields = {"slug": ("video_card_capacity",)}
    list_per_page = 200 #max post per page
    list_max_show_all = 50 #max posts after clicking on hyperref
    view_on_site = True
    empty_value_display = 'unknown' #empty one of values

    save_on_top = True




admin.site.register(Screen, ScreenAdmin)  # in order to show it in django-admin
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

