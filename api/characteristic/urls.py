import imp
from django.urls import path, include
from .views import ProductCharacteristicView, ProductImageView

from .screen import urls as screen_urls
from .processor import urls as processor_urls
from .memory import urls as memory_urls
from .video_card import urls as video_urls
from .product_type import urls as product_type_urls
from .country_brand_made import urls as country_urls
from .brand import urls as brand_urls


urlpatterns = [
    path("brand/", include(brand_urls)),
    path("product_type/", include(product_type_urls)),
    path("country/", include(country_urls)),
    path("screen/", include(screen_urls)),
    path("processor/", include(processor_urls)),
    path("memory/", include(memory_urls)),
    path("video-card/", include(video_urls)),
    path(
        "product_characteristic/<product_id>/",
        ProductCharacteristicView.as_view(),
        name="get_product_characteristics",
    ),
    path(
        "create_product_characteristic/",
        ProductCharacteristicView.as_view(),
        name="create_product_characteristic",
    ),
    path(
        "update_product_characteristic/<product_id>/",
        ProductCharacteristicView.as_view(),
        name="update_product_characteristic",
    ),
    path("<pk>/images/", ProductImageView.as_view(), name="get_product_images"),
]
