from django.urls import path
from .views import ProcessorTypeView, OperationSystemView


urlpatterns = [
    path("get_processor/<pk>/", ProcessorTypeView.as_view(), name="get_processor"),
    path("get_processor/", ProcessorTypeView.as_view(), name="get_processors"),
    path("create_processor/", ProcessorTypeView.as_view(), name="create_processor"),
    path("update_processor/<pk>/", ProcessorTypeView.as_view(),
         name="update_processor"),
    path("delete_processor/<pk>/", ProcessorTypeView.as_view(),
         name="delete_processor"),
    #
    # operation_system
    #
    path("get_oper_system/<pk>/", OperationSystemView.as_view(),
         name="get_oper_system"),
    path("get_oper_system/", OperationSystemView.as_view(), name="get_oper_systems"),
    path(
        "create_oper_system/", OperationSystemView.as_view(), name="create_oper_system"
    ),
    path(
        "update_oper_system/<pk>/",
        OperationSystemView.as_view(),
        name="update_oper_system",
    ),
    path(
        "delete_oper_system/<pk>/",
        OperationSystemView.as_view(),
        name="delete_oper_system",
    ),
]
