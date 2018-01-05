# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from utils import encryption_function, decryption_function
from models import SecretModel
from django.http import HttpResponse

# Create your views here.

def save_secret(request):
    username = request.GET['username']
    value = request.GET['secret']
    ss = SecretModel(username=username, normal_value = value, encrypted_value = encryption_function(value))
    ss.save()
    return HttpResponse("<h2> Saved </h2>")

def get_secret(request):
    username = request.GET['username']
    ss = SecretModel.objects.filter(username=username)
    return HttpResponse("<h2>username :%s password: %s </h2>"%(ss[0].username,decryption_function(ss[0].encrypted_value) ))
    
