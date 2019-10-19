from django.db import models

# Create your models here.

class mymodel(models.Model):
     index = models.IntegerField(default=0)
     description = models.CharField(max_length=50)
     code = models.CharField(max_length=20)

class principal(models.Model):
     p_name = models.CharField(max_length=50)
     def __str__(self):
          return self.p_name

class teacher(models.Model):
     t_name = models.CharField(max_length=50)
     def __str__(self):
          return self.t_name

class student(models.Model):
     name = models.CharField(max_length=50)
     c_lass = models.CharField(max_length=50)
     tea = models.ManyToManyField(teacher)
     pri = models.ForeignKey(principal,on_delete=models.PROTECT)
     def __str__(self):
          return self.name
