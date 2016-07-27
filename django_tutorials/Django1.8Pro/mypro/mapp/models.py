from django.db import models

# Create your models here.
class mmodel(models.Model):
      index = models.IntegerField(default=0)
      desc = models.CharField(max_length=50)
      code = models.CharField(max_length=25)
      nmember = models.CharField(max_length=25)

class cmodel(models.Model):
      year = models.IntegerField(default=0)
      name = models.CharField(max_length=50)
      title = models.CharField(max_length=25)
      department = models.CharField(max_length=25)
