# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class SecretModel(models.Model):
      normal_value = models.CharField(max_length=50)
      username = models.CharField(max_length=50)
      encrypted_value = models.CharField(max_length=255)
      def __str__():
         return (username, normal_value, encrypted_value)
