from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    sb1 = models.CharField(max_length=50, blank=True, default='')
    sb2 = models.CharField(max_length=50, blank=True, default='')
    sb3 = models.CharField(max_length=50, blank=True, default='')
    sb4 = models.CharField(max_length=50, blank=True, default='')
    sb5 = models.CharField(max_length=50, blank=True, default='')
    sb6 = models.CharField(max_length=50, blank=True, default='')
    
    
    def __str__(self):
        return self.name