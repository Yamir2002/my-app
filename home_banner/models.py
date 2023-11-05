from django.db import models

# Create your models here.
class HomeBanner(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to='home_banner/images')
    contactNumber = models.CharField(max_length=100, default='', blank=True)
    email = models.CharField(max_length=100, default='', blank=True)
    
    def __str__(self):
        return self.title