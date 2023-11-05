from django.db import models

# Create your models here.
class LargeBanner(models.Model):
    banner_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='large_banner/images')
    banner_description = models.CharField(max_length=100, blank=True, default='')
    contactNumber = models.CharField(max_length=100, default='', blank=True)
    email = models.CharField(max_length=100, default='', blank=True)
    
    def __str__(self):
        return self.banner_name