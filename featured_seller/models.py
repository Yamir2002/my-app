from django.db import models

# Create your models here.
class FeaturedSeller(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to='featuredSeller/images')
    
    
    def __str__(self):
        return self.title