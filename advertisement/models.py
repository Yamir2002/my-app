from django.db import models

# Create your models here.
class Advertisement(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to='advertisement/images')
    contactNumber = models.CharField(max_length=100, default='', blank=True)
    email = models.CharField(max_length=100, default='', blank=True)
    
    def __str__(self):
        return self.title