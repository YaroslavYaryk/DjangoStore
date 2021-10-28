from django.db import models
from django.utils.safestring import mark_safe


class ProductBrand(models.Model):
    """ class of product brand """

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:

        """our model display in django-admin"""
        verbose_name = "Product Brand"
        verbose_name_plural = "Product Brands"
        ordering = ["name"]  # sorting categories at site
    

class ScreenDiagonal(models.Model):
    """ screen diagonal category class"""

    name = models.CharField("diagonal", max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:

        """our model display in django-admin"""
        verbose_name = "Screen Diagonal"
        verbose_name_plural = "Screen diagonals"
        ordering = ["name"]  # sorting categories at site
    

class ScreenType(models.Model):
    """ screen type caegory class """

    name = models.CharField("type", max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:

        """our model display in django-admin"""
        verbose_name = "Screen Type"
        verbose_name_plural = "Screen Types"
        ordering = ["name"]  # sorting categories at site
     

class ScreenFrequency(models.Model):
    """screen frequency category class"""

    frequency_number = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return self.frequency_number


    class Meta:

        """our model display in django-admin"""
        verbose_name = "Screen Frequency"
        verbose_name_plural = "Screen Frequencies"
        ordering = ["frequency_number"]  # sorting categories at site
    


class ProcessorType(models.Model):
    """class of processor category class""" 

    name = models.CharField("processor type", max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:

        """our model display in django-admin"""
        verbose_name = "Processor Type"
        verbose_name_plural = "Processor Types"
        ordering = ["name"]  # sorting categories at site
     


class OperationSystem(models.Model): 
    """operation system category class"""

    name = models.CharField("operation_system", max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)
    description = models.TextField(null=True)
    
    def __str__(self) -> str:
        return self.name 

    class Meta:

        """our model display in django-admin"""
        verbose_name = "Operation System"
        verbose_name_plural = "Operation Systems"
        ordering = ["name"]  # sorting categories at site
        


class MemoryCapacity(models.Model):
    """memory capacity category class"""

    number_of_gigabite = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return self.number_of_gigabite

    class Meta:

        """our model display in django-admin"""
        verbose_name = "Memory Capacity"
        verbose_name_plural = "Memory Capacities"
        ordering = ["number_of_gigabite"]  # sorting categories at site
    

class MemorySlot(models.Model):
    """memory slot class"""

    number_of_slots = models.IntegerField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return str(self.number_of_slots)

    class Meta:

        """our model display in django-admin"""
        verbose_name = "Memory Slot"
        verbose_name_plural = "Memory Slots"
        ordering = ["number_of_slots"]  # sorting categories at site
     

class MemoryType(models.Model):
    """memory type category class"""

    name = models.CharField("memory_type", max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:

        """our model display in django-admin"""
        verbose_name = "Memory Type"
        verbose_name_plural = "Memory Types"
        ordering = ["name"]  # sorting categories at site
    

class DataStorageDevices(models.Model):
    """data storage devices class"""

    hard_drive_capacity = models.IntegerField()
    hard_drive_type = models.CharField(max_length=20)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return f"{self.hard_drive_capacity} {self.hard_drive_type}"

    class Meta:

        """our model display in django-admin"""
        verbose_name = "Storage Device"
        verbose_name_plural = "Storage Devices"
        ordering = ["hard_drive_capacity", "hard_drive_type"]  # sorting categories at site


class VideoCard(models.Model):
    """video card class"""

    video_card = models.CharField(max_length=100) 
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return self.video_card

    class Meta:

        """our model display in django-admin"""
        verbose_name = "Video Card"
        verbose_name_plural = "Video Cards"
        ordering = ["video_card"]         

class VideoCardMemory(models.Model): #in order to filter by this
    """ class of vdeo card memory (capacity) """

    video_card_capacity = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return self.video_card_capacity

    class Meta:

        """our model display in django-admin"""
        verbose_name = "Video Card Memory"
        verbose_name_plural = "Video Card Memories"
        ordering = ["video_card_capacity"]     

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

    class Meta:

        """our model display in django-admin"""
        verbose_name = "Product Type"
        verbose_name_plural = "Product Types"
        ordering = ["name"]           

class CountryMade(models.Model):
    """country where product was made"""

    name = models.CharField(max_length=255)
    flag = models.ImageField(upload_to="country_made_flags/Data%y/%m/%d/", null=True, blank=True)        
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:

        """our model display in django-admin"""
        verbose_name = "Country Made"
        verbose_name_plural = "Countries Made"
        ordering = ["name"]      

class CountryBrand(models.Model):
    """country where brand was founded"""

    name = models.CharField(max_length=255)
    flag = models.ImageField(upload_to="country_brand__flags/Data%y/%m/%d/", null=True, blank=True)        
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return f"{self.name}" 


    class Meta:

        """our model display in django-admin"""
        verbose_name = "Country Brand"
        verbose_name_plural = "Countries Brand"
        ordering = ["name"]     