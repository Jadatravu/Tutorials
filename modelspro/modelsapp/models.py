from django.db import models

# Create your models here.


class Address(models.Model):
    H_No = models.CharField(max_length=30)
    Line1 = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    colony = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    pin = models.IntegerField()

class JobTitle(models.Model):
    title = models.CharField(max_length=30)

class Department(models.Model):
    dep_name = models.CharField(max_length=30)

class Supervisor(models.Model):
    sup_id = models.IntegerField()

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sur_name = models.CharField(max_length=30)
    email = models.EmailField()
    emp_id = models.IntegerField()
    supervisor = models.ForeignKey(Supervisor)
    department = models.ForeignKey(Department)
    job_title = models.ForeignKey(JobTitle)
    phone = models.IntegerField()
#   picture = models.CharField(max_length=30)
    picture = models.FileField(upload_to='tmp/')
    address = models.OneToOneField(Address)
