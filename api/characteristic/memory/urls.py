from django.urls import path
from .views import (
    MemoryCapacityView,
    MemorySlotView,
    MemoryTypeView,
    DataStorageDevicesView,
)


urlpatterns = [
    #
    # ram capacity
    #
    path(
        "get_ram_capacity/<pk>/", MemoryCapacityView.as_view(), name="get_ram_capacity"
    ),
    path("get_ram_capacity/", MemoryCapacityView.as_view(),
         name="get_ram_capacities"),
    path(
        "create_ram_capacity/", MemoryCapacityView.as_view(), name="create_ram_capacity"
    ),
    path(
        "update_ram_capacity/<pk>/",
        MemoryCapacityView.as_view(),
        name="update_ram_capacity",
    ),
    path(
        "delete_ram_capacity/<pk>/",
        MemoryCapacityView.as_view(),
        name="delete_ram_capacity",
    ),
    #
    # ram type
    #
    path("get_ram_type/<pk>", MemoryTypeView.as_view(), name="get_ram_type"),
    path("get_ram_type/", MemoryTypeView.as_view(), name="get_ram_types"),
    path("create_ram_type/", MemoryTypeView.as_view(), name="create_ram_type"),
    path(
        "update_update_ram_type/<pk>/",
        MemoryTypeView.as_view(),
        name="update_ram_type",
    ),
    path(
        "delete_ram_type/<pk>/",
        MemoryTypeView.as_view(),
        name="delete_ram_type",
    ),
    #
    # ram slots
    #
    path("get_ram_slot/<pk>/", MemorySlotView.as_view(), name="get_ram_slot"),
    path("get_ram_slot/", MemorySlotView.as_view(), name="get_ram_slots"),
    path("create_ram_slot/", MemorySlotView.as_view(), name="create_ram_slot"),
    path("update_ram_slot/<pk>/", MemorySlotView.as_view(), name="update_ram_slot"),
    path("delete_ram_slot/<pk>/", MemorySlotView.as_view(), name="delete_ram_slot"),
    #
    # data storage
    #
    path(
        "get_data_storage/<pk>/",
        DataStorageDevicesView.as_view(),
        name="get_data_storage",
    ),
    path(
        "get_data_storage/", DataStorageDevicesView.as_view(), name="get_data_storages"
    ),
    path(
        "create_data_storage/",
        DataStorageDevicesView.as_view(),
        name="create_data_storage",
    ),
    path(
        "update_data_storage/<pk>/",
        DataStorageDevicesView.as_view(),
        name="update_data_storage",
    ),
    path(
        "delete_data_storage/<pk>/",
        DataStorageDevicesView.as_view(),
        name="delete_data_storage",
    ),
]
