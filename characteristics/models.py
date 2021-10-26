from django.db import models

# Create your models here.

class Screen(models.Model):
    """ class of screen characteristic """

    diagonal_screen = models.ForeignKey("ScreenDiagonal",verbose_name="ScreenDiagonal" ,on_delete=models.CASCADE)
    screen_type = models.ForeignKey("ScreenType",verbose_name="ScreenType", on_delete=models.CASCADE)
    screen_frequency = models.ForeignKey("ScreenFrequency", verbose_name="ScreenFrequency", on_delete=models.CASCADE)
    camera = models.CharField('camera', max_length=255)


class ScreenDiagonal(models.Model):
    """ screen diagonal category class"""

    name = models.CharField("diagonal", max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return self.name

class ScreenType(models.Model):
    """ screen type caegory class """

    name = models.CharField("type", max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name

class ScreenFrequency(models.Model):
    """screen frequency category class"""

    frequency_number = models.IntegerField("frequency")
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return self.name


class Processor(models.Model):
    """processor class"""

    name = models.ForeignKey("ProcessorType", verbose_name=("ProcessorType"), on_delete=models.CASCADE)
    operation_system = models.ForeignKey("OperationSystem", verbose_name=("OperationSystem"), on_delete=models.CASCADE)
    description = models.TextField(null=True)
    

class ProcessorType(models.Model):
    """class of processor category class""" 

    name = models.CharField("processoetype", max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return self.name


class OperationSystem(models.Model): 
    """operation system category class"""

    name = models.CharField("operation_system", max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)
    description = models.TextField(null=True)
    
    def __str__(self) -> str:
        return self.name


class RandomAccessMemory(models.Model):
    """operative memory class"""

    memory_capacity = models.ForeignKey("MemoryCapacity", verbose_name=("MemoryCapacity"), on_delete=models.CASCADE)
    memory_slots = models.ForeignKey("MemorySlot", verbose_name=("MemorySlot"), on_delete=models.CASCADE)
    memory_type = models.ForeignKey("MemoryType", verbose_name=("NemoryType"), on_delete=models.CASCADE)


class MemoryCapacity(models.Model):
    """memory capacity category class"""

    number_of_gigabite = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)


class MemorySlot(models.Model):
    """memory slot class"""

    number_of_slots = models.IntegerField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)


class MemoryType(models.Model):
    """memory type category class"""

    name = models.CharField("memory_type", max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

class DataStorageDevices(models.Model):
    """data storage devices class"""

    hard_drive_capacity = models.IntegerField()
    hard_drive_type = models.CharField(max_length=20)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)


class VideoCard(models.Model):
    """video card class"""

    video_card = models.CharField(max_length=100) 
    videocard_memory = models.ForeignKey("VideoCardMemory", verbose_name=("VideoCardMemory"),
                                    on_delete=models.CASCADE, null=True)       
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)


class VideoCardMemory(models.Model): #in order to filter by this
    """ class of vdeo card memory (capacity) """

    video_card_capacity = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)


class Corp(models.Model):
    """corpus class"""

    color = models.ForeignKey("ColorCorp", verbose_name=("ColorCorp"), on_delete=models.CASCADE)
    weight = models.IntegerField()
    battery = models.ForeignKey("Battery", verbose_name=("Battery"), on_delete=models.CASCADE)
    manipulators = models.CharField(max_length=50)
    height = models.IntegerField()
    width = models.IntegerField()
    depth = models.IntegerField()
    corp_material = models.CharField(max_length=100)


class ColorCorp(models.Model):
    """class of color of corpus"""

    color_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)


class Battery(models.Model):
    """battery class"""

    name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    description = models.TextField(null=True)                            


class Connection(models.Model):
    """connection class"""

    network_adapters = models.CharField(max_length=255)
    wireless_connection = models.CharField(max_length=255)
    input_output = models.CharField(max_length=255)


class ProductType(models.Model):
    """type of prosuct class"""

    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)
    icon = models.ImageField(
        upload_to="icons/Data%y/%m/%d/", null=True, blank=True)     

class CountryMade(models.Model):
    """country where product was made"""

    name = models.CharField(max_length=255)
    flag = models.ImageField(upload_to="country_made_flags/Data%y/%m/%d/", null=True, blank=True)        
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)


class CountryBrand(models.Model):
    """country where brand was founded"""

    name = models.CharField(max_length=255)
    flag = models.ImageField(upload_to="country_brand__flags/Data%y/%m/%d/", null=True, blank=True)        
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)
                       