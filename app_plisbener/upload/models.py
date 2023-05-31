from django.db import models
from cloudinary.models import CloudinaryField

class photos(models.Model): 
    title = models.CharField(max_length = 100)
    image = CloudinaryField('image')

class Images(models.Model):
    title = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = "images/")
    
    def __str__(self):
        return self.title