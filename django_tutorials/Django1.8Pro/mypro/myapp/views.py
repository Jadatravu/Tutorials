from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from myapp.models import mymodel
from myapp.models import contacts
import logging
logger = logging.getLogger(__name__)
# Create your views here.
def hello(request):
    logger.debug("This is debug message")
    logger.error("This is error message")
    return render_to_response("hello.html")

def home(request):
    if request.method == 'GET':
         value_var1= request.GET['var1']
         value_var2= request.GET['var2']
         value_var3= request.GET['var3']
         my_model  = mymodel(index=int(value_var1), description=value_var2, code = value_var3)
         my_model.save()
    return HttpResponse("<h2>Values Entered<br> val_var 1 : %s <br>val_var 2 :%s <br> val_var3: %s</h2>"%(value_var1, value_var2, value_var3))
    #return render_to_response("hello.html")

def data_home(request):
    result = str("<html><body><table border=1>")
    result = result+ str("<tr><th>Index</th><th>Description</th><th>Code</th></tr>")
    for mm in mymodel.objects.all():
          result = result + str("<h2><tr><td>%s</td><td>%s</td><td>%s</td></tr></h2>"%(str(mm.index),mm.description,mm.code))
    result = result+str("</table></body></html>")
    return HttpResponse(result)

def ex_cert(request):
    if request.method == 'GET':
         value_var1= request.GET['id']
         c = contacts.objects.get(id=int(value_var1))
         c_di= {'name':c.name,'department':c.department,'title':c.title,'year':c.year }
    return render_to_response("contacts.html",c_di)
         
