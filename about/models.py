from django.db import models

# Create your models here.
class Andrea(models.Model):
    name = models.CharField(max_length=50, unique=True)
    job = models.CharField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    biography = models.TextField()
    
    def __str__(self):
        return self.name

class Collaboration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    project_idea = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Collaboration request from {self.name}"