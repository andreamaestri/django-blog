from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Andrea(models.Model):
    name = models.CharField(max_length=50, unique=True)
    job = models.CharField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    biography = HTMLField()
    
    def __str__(self):
        return self.name