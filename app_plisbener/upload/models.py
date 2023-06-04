from django.db import models
from cloudinary.models import CloudinaryField

class photos(models.Model): 
    title = models.CharField(max_length = 100)
    image = CloudinaryField('image',
                            overwrite = True,
                            resource_type = 'image',
                            use_filename = True,
                            unique_filename = False)