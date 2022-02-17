from django.urls import path
from .views import VideoCardView, VideoCardMemoryView


urlpatterns = [
    path("get_card/<pk>/", VideoCardView.as_view(), name="get_card"),
    path("get_card/", VideoCardView.as_view(), name="get_cards"),
    path("create_card/", VideoCardView.as_view(), name="create_card"),
    path("update_card/<pk>/", VideoCardView.as_view(), name="update_card"),
    path("delete_card/<pk>/", VideoCardView.as_view(), name="delete_card"),
    # screen type
    path("get_memory/<pk>/", VideoCardMemoryView.as_view(), name="get_memory"),
    path("get_memory/", VideoCardMemoryView.as_view(), name="get_memory"),
    path("create_memory/", VideoCardMemoryView.as_view(), name="create_memory"),
    path("update_memory/<pk>/", VideoCardMemoryView.as_view(), name="update_memory"),
    path("delete_memory/<pk>/", VideoCardMemoryView.as_view(), name="delete_memory"),
]
