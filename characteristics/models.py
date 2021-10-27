from django.db import models


class ProductBrand(models.Model):
    """ class of product brand """

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)
    description = models.TextField(null=True)

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

    frequency_number = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return self.frequency_number


class ProcessorType(models.Model):
    """class of processor category class""" 

    name = models.CharField("processor type", max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)
    description = models.TextField(null=True)

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


class MemoryCapacity(models.Model):
    """memory capacity category class"""

    number_of_gigabite = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return self.number_of_gigabite

class MemorySlot(models.Model):
    """memory slot class"""

    number_of_slots = models.IntegerField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return str(self.number_of_slots)

class MemoryType(models.Model):
    """memory type category class"""

    name = models.CharField("memory_type", max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return self.name

class DataStorageDevices(models.Model):
    """data storage devices class"""

    hard_drive_capacity = models.IntegerField()
    hard_drive_type = models.CharField(max_length=20)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return f"{self.hard_drive_capacity} {self.hard_drive_type}"

class VideoCard(models.Model):
    """video card class"""

    video_card = models.CharField(max_length=100) 
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return self.video_card

class VideoCardMemory(models.Model): #in order to filter by this
    """ class of vdeo card memory (capacity) """

    video_card_capacity = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return self.video_card_capacity

class ProductType(models.Model):
    """type of prosuct class"""

    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)
    icon = models.ImageField(
        upload_to="icons/Data%y/%m/%d/", null=True, blank=True)   

    def __str__(self) -> str:
        return self.name      

class CountryMade(models.Model):
    """country where product was made"""

    name = models.CharField(max_length=255)
    flag = models.ImageField(upload_to="country_made_flags/Data%y/%m/%d/", null=True, blank=True)        
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return self.name

class CountryBrand(models.Model):
    """country where brand was founded"""

    name = models.CharField(max_length=255)
    flag = models.ImageField(upload_to="country_brand__flags/Data%y/%m/%d/", null=True, blank=True)        
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return self.name                   