# Create your views here.
from django.http import HttpResponse
from django.template import Context
from django.template import loader
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login

from crud.models import Author
from crud.models import Publisher

def add_pub_form(request):
    c={}
    c.update(csrf(request))
    return render_to_response("addpublisher.html",c)

def add_pub(request):
    c={}
    c.update(csrf(request))
    pubName = request.POST["name"]
    pub = Publisher(name=pubName)
    pub.save()
    pubList = Publisher.objects.all()
    template = loader.get_template("listpublisher.html")
    #template = loader.get_template("login.html")
    context = RequestContext(request,{
       'pub_list':pubList,
       'csrf_token':c,
    })
    return HttpResponse(template.render(context))
    #return render_to_response("listpublisher.html",pubList,c)

def list_pub(request):
    c={}
    c.update(csrf(request))
    pubList = Publisher.objects.all()
    template = loader.get_template("listpublisher.html")
    context = RequestContext(request,{
       'pub_list':pubList,
       'csrf_token':c,
    })
    return HttpResponse(template.render(context))

def edit_save_op(request):
    c={}
    c.update(csrf(request))
    pubList = Publisher.objects.all()
    for pub in pubList:
        id = pub.id
        action_str = str("name_")+str(id)
        display_str = str("display_")+str(id)
        if(request.POST.keys().__contains__(action_str)):
            if( request.POST[action_str] == display_str ):
                primaryKey = id
    name=request.POST["username"]
    publi = Publisher.objects.get(pk=primaryKey)
    publi.name = name
    publi.save()
    template = loader.get_template("listpublisher.html")
    #template = loader.get_template("login.html")
    context = RequestContext(request,{
       'pub_list':pubList,
       'csrf_token':c,
    })
    return HttpResponse(template.render(context))

def edit_del_op(request):
    c={}
    c.update(csrf(request))
    html = ""
    primaryKey = 0 
    #for key in request.POST.keys():
    #     html = html + key
    pubList = Publisher.objects.all()
    for pub in pubList:
        id = pub.id
        action_str = str("action_")+str(id)
        display_str = str("display_")+str(id)
        #html = html + str(" : ") + action_str + str(" : ") + display_str
        if(request.POST.keys().__contains__(action_str)):
            if( request.POST[action_str] == display_str ):
                primaryKey = id
    if 'name_edit' in request.POST.keys():
        pub = Publisher.objects.filter(pk=primaryKey)
        template = loader.get_template("edit.html")
        context = RequestContext(request,{
          'pname':pub[0].name,
          'pkey':primaryKey,
          'csrf_token':c,
        })
        return HttpResponse(template.render(context))
        #html = html + "edit selected" + str(primaryKey)
    elif 'name_delete' in request.POST.keys():
        html = html + "record with primary key :" + str(primaryKey) +str(" deleted")
        pub = Publisher.objects.filter(pk=primaryKey)
        pub.delete()
    return HttpResponse(html,c)
    #return render_to_response("addpublisher.html",c)
