from django.db import models

# Create your models here.
class mymodel(models.Model):
     index = models.IntegerField(default=0)
     description = models.CharField(max_length=50)
     code = models.CharField(max_length=50)

class contacts(models.Model):
     name = models.CharField(max_length=50)
     title = models.CharField(max_length=50)
     department = models.CharField(max_length=50)
     year = models.IntegerField(default=0)

class principal(models.Model):
     p_name = models.CharField(max_length=50)

class teacher(models.Model):
     t_name = models.CharField(max_length=50)

class student(models.Model):
     name = models.CharField(max_length=50)
     c_lass = models.CharField(max_length=50)
     tea = models.ManyToManyField(teacher)
     pri = models.ForeignKey(principal)
