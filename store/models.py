from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.forms import IntegerField
from characteristics.models import (
    CountryBrand,
    CountryMade,
    DataStorageDevices,
    MemoryCapacity,
    MemorySlot,
    MemoryType,
    OperationSystem,
    ProcessorType,
    ProductBrand,
    ProductType,
    ScreenDiagonal,
    ScreenFrequency,
    ScreenType,
    VideoCard,
    VideoCardMemory,
)
from django.conf import settings

# Create your models here.


class Product(models.Model):
    """class of single product"""

    name = models.CharField("name", max_length=255)
    only_name = models.CharField("only_name", max_length=255, null=True)
    # characteristics = models.ForeignKey("Characteristics", name="characteristics", on_delete=models.CASCADE)
    description = models.TextField("description", blank=True)
    short_description = models.TextField(null=True)
    brand = models.ForeignKey(
        ProductBrand,
        verbose_name=("Brand of product"),
        on_delete=models.CASCADE,
        null=True,
    )
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL", null=True
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    updation_date = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="photos/Data%y/%m/%d/", blank=True)
    video = models.FileField(upload_to="videos/Data%y/%m/%d/", blank=True)
    is_published = models.BooleanField(default=True)  # default is True
    type_of_product = models.ForeignKey(
        ProductType, verbose_name=("ProductType"), on_delete=models.CASCADE, null=True
    )
    country_made = models.ForeignKey(
        CountryMade, verbose_name=("CountryMade"), on_delete=models.CASCADE, null=True
    )
    country_brand = models.ForeignKey(
        CountryBrand, verbose_name=("CountryBrand"), on_delete=models.CASCADE, null=True
    )
    warranty = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


class Characteristics(models.Model):
    """Characteristic class"""

    product = models.ForeignKey(
        "Product", verbose_name=("Product"), on_delete=models.CASCADE, null=True
    )

    # Screen
    diagonal_screen = models.ForeignKey(
        ScreenDiagonal,
        verbose_name="Screen diagonal",
        on_delete=models.CASCADE,
        null=True,
    )
    screen_type = models.ForeignKey(
        ScreenType, verbose_name=("Screen type"), on_delete=models.CASCADE, null=True
    )
    screen_frequency = models.ForeignKey(
        ScreenFrequency,
        verbose_name=("Screen frequency"),
        on_delete=models.CASCADE,
        null=True,
    )
    camera = models.CharField("camera", max_length=255, null=True, blank=True)

    # Processor
    processor_name = models.ForeignKey(
        ProcessorType,
        verbose_name=("Processor type"),
        on_delete=models.CASCADE,
        null=True,
    )
    operation_system = models.ForeignKey(
        OperationSystem,
        verbose_name=("Operation system"),
        on_delete=models.CASCADE,
        null=True,
    )

    # RAM (RandomAccessMemory)
    memory_capacity = models.ForeignKey(
        MemoryCapacity,
        verbose_name=("Memory capacity"),
        on_delete=models.CASCADE,
        null=True,
    )
    memory_slots = models.ForeignKey(
        MemorySlot, verbose_name=("Memory slots"), on_delete=models.CASCADE, null=True
    )
    memory_type = models.ForeignKey(
        MemoryType, verbose_name=("Nemory type"), on_delete=models.CASCADE, null=True
    )

    # hard drive
    data_storage = models.ForeignKey(
        DataStorageDevices,
        verbose_name=("Hard drive capacity"),
        on_delete=models.CASCADE,
        null=True,
    )

    # Video Card
    video_card = models.ForeignKey(
        VideoCard, verbose_name=("Video card"), on_delete=models.CASCADE, null=True
    )
    video_card_memory = models.ForeignKey(
        VideoCardMemory,
        verbose_name=("Video card memory"),
        on_delete=models.CASCADE,
        null=True,
    )

    # corpus
    color = models.CharField(max_length=255, null=True)
    weight = models.FloatField(null=True)
    battery = models.CharField(max_length=255, null=True)
    manipulators = models.CharField(max_length=50, null=True)
    height = models.FloatField(null=True)
    width = models.FloatField(null=True)
    depth = models.FloatField(null=True)
    corp_material = models.CharField(max_length=100, null=True)

    # connection adapter
    network_adapters = models.CharField(max_length=255, null=True)
    wireless_connection = models.CharField(max_length=255, null=True)
    input_output = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.product.name


class CommentResponse(models.Model):
    post = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="comment_response"
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("created",)

    def __str__(self):
        return "Comment by {} on {}".format(self.name, self.post)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.FileField("images", upload_to="photos/Data%y/%m/%d/")

    def __str__(self):
        return self.product.name

    class Meta:

        """our model display in django-admin"""

        verbose_name = "Image"
        verbose_name_plural = "Images"
        ordering = ["id"]  # sorting categories at site


class ProductLike(models.Model):

    """add like to our post"""

    post = models.ForeignKey(
        Product, related_name="likes", on_delete=models.CASCADE, null=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="likes",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return f"{self.post.only_name} {self.user.username}"


class CartProduct(models.Model):
    """class of product-cart for user"""

    user = models.CharField(max_length=100, null=True)

    cart = models.ForeignKey(
        "Cart",
        verbose_name=("Cart"),
        on_delete=models.CASCADE,
        related_name="related_product",
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    quantity = models.PositiveIntegerField(default=1)
    total_price = models.PositiveBigIntegerField(default=0, verbose_name="Total price")

    def __str__(self):
        return f"CartProduct( {self.user} {self.content_object.only_name} )"


class Cart(models.Model):
    """class of cart of products"""

    owner = models.CharField(max_length=100, null=True)

    products = models.ManyToManyField(
        CartProduct, blank=True, related_name="related_cart"
    )
    total_products = models.PositiveIntegerField(default=0)
    total_price = models.PositiveBigIntegerField(default=0, verbose_name="Total price")
    in_order = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.owner} {self.products}"


class Coupon(models.Model):
    """class of coupone {code: discount}"""

    coupon_code = models.CharField("coupon", max_length=100)
    discount = models.PositiveIntegerField("discount", default=0)

    def __str__(self):
        return f"{self.coupon_code} - {self.discount}"


class UserCoupon(models.Model):
    """class of coupone {code: discount}"""

    ip = models.CharField(max_length=100, null=True)

    coupon = models.ForeignKey(
        Coupon, verbose_name=("Coupon"), on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return f"{self.ip} - {self.coupon}"


class UserSearchHistory(models.Model):
    """class of user search history"""

    ip = models.CharField(max_length=100, null=True)

    search_value = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user} - '{self.search_value}'"


class IpModel(models.Model):

    """class for getting ip adress of anyone"""

    product = models.ForeignKey(
        Product, related_name="ip", on_delete=models.CASCADE, null=True
    )
    ip = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ip}"


class UserOrderHistory(models.Model):
    """class of user sort history"""

    ip = models.CharField(max_length=100, null=True)
    order_place = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ip} - '{self.order_place}'"


class ProductCommentPhotos(models.Model):
    """class of user sort history"""

    photo = models.FileField("images", upload_to="photos/Data%y/%m/%d/")

    def __str__(self):
        return f"{self.photo}'"


class ProductComment(models.Model):

    """Model for creating comment part"""

    product = models.ForeignKey(
        Product, related_name="all_comments", on_delete=models.CASCADE
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    pros = models.TextField(max_length=200, blank=True)
    cons = models.TextField(max_length=200, blank=True)
    photos = models.ManyToManyField(
        ProductCommentPhotos, verbose_name=("commentPhotos"), blank=True
    )
    rating = models.IntegerField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.comment[:30]

    def get_comment_likes(self):
        return self.likes.count()

    def children(self):
        return ProductComment.objects.filter(parent=self)

    class Meta:

        """our model display in django-admin"""

        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ["creation_date"]  # sorting categories at site


class LikedComment(models.Model):
    """Class container thats gonna consist user that already liked comment"""

    post_comment = models.ForeignKey(
        ProductComment, related_name="likes_comment", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="likes_comment", on_delete=models.CASCADE
    )

    def __str__(self):
        return (
            str(self.post_comment)
            if len(str(self.post_comment)) < 100
            else str(self.post_comment)[:100]
        )
