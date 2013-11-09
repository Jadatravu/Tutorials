# Create your views here.
from django.http import HttpResponse
from django.template import Context
from django.template import loader
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth import logout

from django.contrib.auth import authenticate, login
 
from books.models import Book
from books.models import Publisher

def index(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password= password)
    html = ''
    if user is not None:
        if user.is_active:
              #login(request,user)
              #publisherList = Publisher.objects.all()
              #for publisher in publisherList:
              #    html = html + str(publisher.name) + str(' ')
              html = html + str("User logged in")
              #html = html + str("<a href=\"http://127.0.0.1:8000/logout\">logout</a>")
              html = html + str("<a href=\"/logout/\">logout</a>")
        else:
            html="disabled account"
    else:
        html = " Invalid login"
    
    #return render_to_response(html)
    return HttpResponse(html)

def my_index(request):
    html = ''
    if request.user.is_authenticated():
              publisherList = Publisher.objects.all()
              for publisher in publisherList:
                  html = html + str(publisher.name) + str(' ')
    else:
        html = " user is not authenticated"
    
    #return render_to_response(html)
    return HttpResponse(html)

def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response("login.html",c)

def logout(request):
    logout(request)
