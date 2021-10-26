from django.db import connection, models

from characteristics.models import Connection, Corp, CountryBrand, \
    CountryMade, DataStorageDevices, Processor, ProductType, RandomAccessMemory, Screen, VideoCard

# Create your models here.

class Product(models.Model):
    """ class of single product """

    name = models.CharField("name", max_length=255)
    # characteristics = models.ForeignKey("Characteristics", name="characteristics", on_delete=models.CASCADE)
    description = models.TextField("description", blank=True)
    short_description = models.TextField(null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    updation_date = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="photos/Data%y/%m/%d/", blank=True)
    video = models.FileField(upload_to="videos/Data%y/%m/%d/", blank=True)
    is_published = models.BooleanField(default=True)  # default is True   
    type_of_product = models.ForeignKey(ProductType, verbose_name=("ProductType"), 
                                        on_delete=models.CASCADE, null=True)   
    country_made = models.ForeignKey(CountryMade, verbose_name=("CountryMade"), 
                                        on_delete=models.CASCADE, null=True)
    country_brand = models.ForeignKey(CountryBrand, verbose_name=("CountryBrand"), 
                                        on_delete=models.CASCADE, null=True)
    warranty = models.IntegerField(null=True)


class Characteristics(models.Model):
    """ Characteristic class """

    product = models.ForeignKey("Product", verbose_name=("Product"),
                                on_delete=models.CASCADE, null=True)

    screen = models.ForeignKey(Screen, verbose_name="Screen", 
                                on_delete=models.CASCADE, null=True)
    processor = models.ForeignKey(Processor, verbose_name=("Processor"),
                                on_delete=models.CASCADE, null=True)
    random_access_memory = models.ForeignKey(RandomAccessMemory,
                                verbose_name=("RandomAccessMemory"), 
                                on_delete=models.CASCADE, null=True)   
    data_storage = models.ForeignKey(DataStorageDevices, verbose_name=("DataStorageDevices"),
                                on_delete=models.CASCADE, null=True)
    video_card = models.ForeignKey(VideoCard, verbose_name=("VideoCard"),
                                on_delete=models.CASCADE, null=True)
    corpus = models.ForeignKey(Corp, verbose_name=("Corp"),
                                on_delete=models.CASCADE, null=True)  
    connection = models.ForeignKey(Connection, verbose_name=("Connection"),
                                on_delete=models.CASCADE, null=True)                                                          


                       
class CommentResponse(models.Model): 
    post = models.ForeignKey(Product,
                             on_delete=models.CASCADE,
                             related_name='comment_response')
    name = models.CharField(max_length=80) 
    email = models.EmailField() 
    body = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True) 

    class Meta: 
        ordering = ('created',) 

    def __str__(self): 
        return 'Comment by {} on {}'.format(self.name, self.post) 


class WomanImage(models.Model):
    post = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to="photos/Data%y/%m/%d/")

    def __str__(self):
        return self.post.name

    class Meta:

        """our model display in django-admin"""
        verbose_name = "Image"
        verbose_name_plural = "Images"
        ordering = ["id"]  # sorting categories at site