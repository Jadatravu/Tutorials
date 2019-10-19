from django.shortcuts import render
from django.shortcuts import render_to_response

from .models import mymodel,student,teacher,principal
from django.http import HttpResponse
# Create your views here.

from .forms import mform,sform


def c_view(request):
    tea_name = request.GET["teacher"]
    tea_set = teacher.objects.filter(t_name = tea_name)
    print(len(tea_set))
    if len(tea_set) > 0:
        s_set = tea_set[0].student_set.all()
        print(len(s_set))
        return render_to_response('m3.html',{'students':s_set})
    else:
        return HttpResponse("no teacher with name found")
    
def form_view1(request):
    if request.method == 'POST':
        form = sform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = sform()
    return render_to_response('m2.html',{'form':form})

def form_view(request):
    if request.method == 'POST':
        form = mform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = mform()
    return render_to_response('m1.html',{'form':form})

def myfunc(request):
    item1 = request.GET['var1']
    item2 = request.GET['var2']
    item3  = request.GET['var3']
    m1 = mymodel(index = item2,description=item1,code = item3)
    m1.save()
    return HttpResponse("<h2> values inserted </h2>")
    
def myfunc1(request):
    var_location = request.GET['var1']
    var_department = request.GET['var2']
    var_name = request.GET['var3']
    var_from = request.GET['var4']
    print (var_department)
    return render_to_response('t.html',{'branch_location':var_location,\
                                        'department':var_department,\
                                        'name':var_name,\
                                        'from':var_from})

def myfunc2(request):
    return render_to_response('t1.html',{})
