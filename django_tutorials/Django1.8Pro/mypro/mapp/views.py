from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from mapp.models import mmodel
from mapp.models import cmodel
"""
from mapp.models import mmodel1
from mapp.models import mmodel2
"""

# Create your views here.

def myviewfunc(request):
    result = str("<table border =1>")
    m_a = mmodel.objects.all()
    for m_i in m_a:
        result = result + str("<tr><td>%s</td><td>%s</td><td>%s</td></tr>"%(str(m_i.index),m_i.desc, m_i.code))
    result = result + str("</table>")
        
    #return HttpResponse("<h2> My  Hello world </h2>")
    return HttpResponse(result)

def myview_second_func(request):
    result = {}
    if request.method == 'GET':
        value_var1 = request.GET['var1']
        value_var2 = request.GET['var2']
        value_var3 = request.GET['var3']
        #mmodel_i = mmodel(index=int(value_var1),desc=value_var2, code=value_var3)
        #mmodel_i.save()
        result['string1'] = value_var1
        result['string2'] = value_var2
        result['string3'] = value_var3
      
    return render_to_response("hello.html", result)
    #return HttpResponse("<h2> var1 : %s <br> var2 : %s <br>var3 :%s<br></h2>"%(value_var1,value_var2,value_var3))

def my_template_view(request):        
    result = {}
    if request.method == 'GET':
        value_var1 = request.GET['id']
        c_i  = cmodel.objects.get(id = int(value_var1))
        result['name'] = c_i.name
        result['department'] = c_i.department
        result['title'] = c_i.title
        result['year'] = c_i.year
    return render_to_response("contacts.html", result)
       
