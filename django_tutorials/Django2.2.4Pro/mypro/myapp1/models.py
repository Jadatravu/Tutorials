from django.db import models

# Create your models here.

class m_model(models.Model):
     i_d = models.IntegerField(default=0)
     description = models.CharField(max_length=50)
     code = models.CharField(max_length=50)
