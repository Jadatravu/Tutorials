from django.shortcuts import render
from django.http import HttpResponse
from myapp1.models import mymodel

# Create your views here.

def hello(request):
    return HttpResponse("<h2> This is my First Django Program </h2>")

def idata(request):
    var1_value = request.GET['var1']
    var2_value = request.GET['var2']
    m1 = mymodel(pid=var1_value, pdescription=var2_value)
    m1.save()
    return HttpResponse("<h2> Data Inserted </h2>")
