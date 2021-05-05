from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=50)

    def __str__(self):
        return self.name
    
