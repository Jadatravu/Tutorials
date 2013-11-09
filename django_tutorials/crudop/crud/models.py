from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=30)

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
