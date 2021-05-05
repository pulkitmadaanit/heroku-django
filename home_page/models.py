from django.db import models

# Create your models here.
class HomeSlider(models.Model):
    image = models.ImageField(upload_to="HomeSlider/images/")
    
