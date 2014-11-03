from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf

from modelsapp.models import Contact
from modelsapp.forms import ContactForm
from modelsapp.models import JobTitle
from modelsapp.forms import JobTitleForm

from modelsapp.models import Department
from modelsapp.forms import DepartmentForm

from modelsapp.models import Supervisor
from modelsapp.forms import SupervisorForm
from modelsapp.forms import ViewContactForm

from modelsapp.models import Address
from modelsapp.forms import ESearchForm

from django.contrib.auth import (REDIRECT_FIELD_NAME, login as auth_login,
    logout as auth_logout, get_user_model, update_session_auth_hash)
from django.contrib.sites.shortcuts import get_current_site
from django.template.response import TemplateResponse

from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm

from django.contrib.auth import authenticate, logout
from django.contrib import auth

import logging
logger = logging.getLogger(__name__)


# Create your views here.
def deletecontactform(request,con_id):
    #if (request.user.is_authenticated() == False):
    if request.user.is_authenticated() and request.user.is_superuser:
        logger.debug ("request user %s is authenticated"%request.user.username)
    else:
        logger.debug ("request user %s is authenticated"%request.user.username)
        c={}
        c.update(csrf(request))
        return render_to_response("login.html",c)
    logger.debug("this is edit contact form")
    contacts = Contact.objects.all()
    con_l = [] 
    for con in contacts:
        if int(con.supervisor.sup_id) == int(con_id):
           logger.debug( con.first_name)
           con_l.append(con)
    logger.debug("contacts len %s"%str(len(con_l)))
    if len(con_l) > 0:
        return render_to_response(
            'deletesupervisor.html',
            {'supcontacts': con_l},
            context_instance=RequestContext(request)
        )#
    else:
        del_contact = Contact.objects.get(id=con_id)
        logger.debug("deleting contact")
        logger.debug( con.first_name)
        del_contact.delete()
        logger.debug("deleted contact")
        return render_to_response(
            'contactdelete.html',
            {'contactid': con_id,'user':request.user},
            context_instance=RequestContext(request)
        )#
def editcontactform(request,con_id):
    #if (request.user.is_authenticated() == False):
    if request.user.is_authenticated() and request.user.is_superuser:
        logger.debug ("request user %s is authenticated"%request.user.username)
    else:
        logger.debug ("request user %s is authenticated"%request.user.username)
        c={}
        c.update(csrf(request))
        return render_to_response("login.html",c)
    logger.debug("this is edit contact form")
    document = Contact.objects.get(id=con_id)
    # Handle file upload
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            picture1 = request.FILES['picture']
            c_id = request.POST['c_id']
            old_pic1 = request.POST['old_pic']
            last_name1 = request.POST['last_name']
            first_name1 = request.POST['first_name']
            sur_name1 = request.POST['sur_name']
            email1 = request.POST['email']
            emp_id1 = request.POST['emp_id']
            phone1 = request.POST['phone']
            supervisor1 = request.POST['supervisor']
            jobtitle1 = request.POST['title']
            department1 = request.POST['department']
            H_No1 = request.POST['H_No']
            Line_1 = request.POST['Line1']
            street1 = request.POST['street']
            colony1 = request.POST['colony']
            city1 = request.POST['city']
            pin1 = request.POST['pin']
            add1 = Address(H_No=H_No1,Line1=Line_1,street=street1,colony=colony1,city=city1,pin=pin1)
            add1.save()
            pin1 = request.POST['pin']
            sup1 = Supervisor.objects.filter(sup_id=supervisor1)[0]
            job1 = JobTitle.objects.filter(title=jobtitle1)[0]
            dep1 = Department.objects.filter(dep_name=department1)[0]
            con_obj = Contact.objects.get(id=c_id)
            if sup1 and job1 and dep1:
               #newdoc = Contact(first_name=first_name1,last_name=last_name1,sur_name=sur_name1,email=email1,emp_id=emp_id1,supervisor=sup1,department=dep1,job_title=job1,phone=phone1,picture=picture1,address=add1)
               #newdoc.save()
               con_obj.first_name = first_name1
               con_obj.last_name = last_name1
               con_obj.sur_name = sur_name1
               con_obj.email = email1
               con_obj.emp_id = emp_id1
               con_obj.supervisor = sup1
               con_obj.department = dep1
               con_obj.job_title = job1
               con_obj.phone = phone1
               con_obj.address = add1
               if picture == None:
                  con_obj.picture = old_pic1
               else:
                  con_obj.picture = picture1 
               con_obj.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('modelsapp.views.editcontact'))
    else:
        default_data={'c_id':document.id,'old_pic':document.picture,'picture':document.picture,'first_name':document.first_name,'last_name':document.last_name,'sur_name':document.sur_name,'email':document.emp_id,'phone':document.phone,'email':document.email,'emp_id':document.emp_id,'H_No':document.address.H_No,'Line1':document.address.Line1,'street':document.address.street,'colony':document.address.colony,'city':document.address.city,'pin':document.address.pin}
        form = ContactForm(default_data) 

    # Load documents for the list page
    #documents = Document.objects.all()
    supervisors = Supervisor.objects.all()
    jobtitle = JobTitle.objects.all()
    department = Department.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'econtactform.html',
        #{'documents': documents, 'form': form},
        {'form': form,'supervisors':supervisors,'jobtitle':jobtitle,'department':department,'supervisor_id':document.supervisor.sup_id, 'jobtitle_name':document.job_title.title, 'department_name':document.department.dep_name,'picture':document.picture},
        context_instance=RequestContext(request)
    )#

def viewcontact(request,con_id):
    #if (request.user.is_authenticated() == False):
    if request.user.is_authenticated():
        logger.debug ("request user %s is authenticated"%request.user.username)
    else:
        logger.debug ("request user %s is authenticated"%request.user.username)
        c={}
        c.update(csrf(request))
        return render_to_response("login.html",c)

    document = Contact.objects.get(id=con_id)

    return render_to_response(
         'viewcontact2.html',
         {'document': document},
         #{'form': form},
         context_instance=RequestContext(request)
    )#
def supervisorform(request):
    if request.user.is_authenticated() and request.user.is_superuser:
        logger.debug ("request user %s is authenticated"%request.user.username)
    else:
        logger.debug ("request user %s is authenticated"%request.user.username)
        c={}
        c.update(csrf(request))
        return render_to_response("login.html",c)
    # Handle file upload
    if request.method == 'POST':
        form = SupervisorForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Supervisor(sup_id = request.POST['sup_id'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('modelsapp.views.supervisorform'))
    else:
        form = SupervisorForm() # A empty, unbound form

    # Load documents for the list page
    documents = Supervisor.objects.all()
    contacts = Contact.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'supervisor.html',
        {'supervisor': documents, 'form': form, 'contacts':contacts,'user':request.user},
        #{'form': form},
        context_instance=RequestContext(request)
    )#
def deletesearchform(request):
    if request.user.is_authenticated() and request.user.is_superuser:
        logger.debug ("request user %s is authenticated"%request.user.username)
    else:
        logger.debug ("request user %s is authenticated"%request.user.username)
        c={}
        c.update(csrf(request))
        return render_to_response("login.html",c)
    if request.method == 'POST':
        form = ESearchForm(request.POST, request.FILES)
        if form.is_valid():
            search_key = request.POST['search_key']
            documents0 = list(Contact.objects.filter(first_name__contains=search_key))
            documents1=list(Contact.objects.filter(last_name__contains=search_key))
            for doc in documents1:
                documents0.append(doc)
            documents2=list(Contact.objects.filter(sur_name__contains=search_key))
            for doc in documents2:
                documents0.append(doc)
            contact_id_list = []
            for doc in documents0:
               if contact_id_list.__contains__(doc.id):
                 pass
               else:
                  contact_id_list.append(doc.id)
            documents = []
            for con_id in contact_id_list:
                con_ob = Contact.objects.get(id=con_id)
                documents.append(con_ob)
            # Redirect to the document list after POST
            #return HttpResponseRedirect(reverse('modelsapp.views.esearchform'))
    else:
        form = ESearchForm() # A empty, unbound form
        documents = None

    # Load documents for the list page
    #documents = Department.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'dsearch.html',
        {'search': documents, 'form': form,'user':request.user},
        #{'form': form},
        context_instance=RequestContext(request)
    )#
def editsearchform(request):
    if request.user.is_authenticated() and request.user.is_superuser:
        logger.debug ("request user %s is authenticated"%request.user.username)
    else:
        logger.debug ("request user %s is authenticated"%request.user.username)
        c={}
        c.update(csrf(request))
        return render_to_response("login.html",c)
    if request.method == 'POST':
        form = ESearchForm(request.POST, request.FILES)
        if form.is_valid():
            search_key = request.POST['search_key']
            documents0 = list(Contact.objects.filter(first_name__contains=search_key))
            documents1=list(Contact.objects.filter(last_name__contains=search_key))
            for doc in documents1:
                documents0.append(doc)
            documents2=list(Contact.objects.filter(sur_name__contains=search_key))
            for doc in documents2:
                documents0.append(doc)
            contact_id_list = []
            for doc in documents0:
               if contact_id_list.__contains__(doc.id):
                 pass
               else:
                  contact_id_list.append(doc.id)
            documents = []
            for con_id in contact_id_list:
                con_ob = Contact.objects.get(id=con_id)
                documents.append(con_ob)
            # Redirect to the document list after POST
            #return HttpResponseRedirect(reverse('modelsapp.views.esearchform'))
    else:
        form = ESearchForm() # A empty, unbound form
        documents = None

    # Load documents for the list page
    #documents = Department.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'esearch.html',
        {'search': documents, 'form': form, 'user':request.user},
        #{'form': form},
        context_instance=RequestContext(request)
    )#
def esearchform(request):
    if request.user.is_authenticated():
        logger.debug ("request user %s is authenticated"%request.user.username)
    else:
        logger.debug ("request user %s is authenticated"%request.user.username)
        c={}
        c.update(csrf(request))
        return render_to_response("login.html",c)
    if request.method == 'POST':
        form = ESearchForm(request.POST, request.FILES)
        if form.is_valid():
            search_key = request.POST['search_key']
            documents0 = list(Contact.objects.filter(first_name__contains=search_key))
            documents1=list(Contact.objects.filter(last_name__contains=search_key))
            for doc in documents1:
                documents0.append(doc)
            documents2=list(Contact.objects.filter(sur_name__contains=search_key))
            for doc in documents2:
                documents0.append(doc)
            contact_id_list = []
            for doc in documents0:
               if contact_id_list.__contains__(doc.id):
                 pass
               else:
                  contact_id_list.append(doc.id)
            documents = []
            for con_id in contact_id_list:
                con_ob = Contact.objects.get(id=con_id)
                documents.append(con_ob)
            # Redirect to the document list after POST
            #return HttpResponseRedirect(reverse('modelsapp.views.esearchform'))
    else:
        form = ESearchForm() # A empty, unbound form
        documents = None

    # Load documents for the list page
    #documents = Department.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'search.html',
        {'search': documents, 'form': form},
        #{'form': form},
        context_instance=RequestContext(request)
    )#
def departmentform(request):
    if request.user.is_authenticated() and request.user.is_superuser:
        logger.debug ("request user %s is authenticated"%request.user.username)
    else:
        logger.debug ("request user %s is authenticated"%request.user.username)
        c={}
        c.update(csrf(request))
        return render_to_response("login.html",c)
    # Handle file upload
    if request.method == 'POST':
        form = DepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Department(dep_name = request.POST['dep_name'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('modelsapp.views.departmentform'))
    else:
        form = DepartmentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Department.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'department.html',
        {'department': documents, 'form': form,'user':request.user},
        #{'form': form},
        context_instance=RequestContext(request)
    )#
def jobtitleform(request):
    if request.user.is_authenticated() and request.user.is_superuser:
        logger.debug ("request user %s is authenticated"%request.user.username)
    else:
        logger.debug ("request user %s is authenticated"%request.user.username)
        c={}
        c.update(csrf(request))
        return render_to_response("login.html",c)
    # Handle file upload
    if request.method == 'POST':
        form = JobTitleForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = JobTitle(title = request.POST['title'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('modelsapp.views.jobtitleform'))
    else:
        form = JobTitleForm() # A empty, unbound form

    # Load documents for the list page
    documents = JobTitle.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'jobtitle.html',
        {'jobtitle': documents, 'form': form,'user':request.user},
        #{'form': form},
        context_instance=RequestContext(request)
    )#

def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response("login.html",c)
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/Contacts/login/")
    #auth_logout(request)


def adminindex(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password= password)
    if user.is_active:
       logger.error ( "error message use rname " + request.user.username)
       logger.debug ( "debug message use rname " + request.user.username)
       auth_login(request, user)
    else:
       logger.debug ( " rname " + request.user.username)
    return render_to_response(
            'adminindex.html',
            {'user':request.user},
            context_instance=RequestContext(request)
    )
    """
    if user.is_superuser:
        return render_to_response(
            'adminindex.html',
            {'user':request.user},
            context_instance=RequestContext(request)
        )
    else:
        return render_to_response(
            'userindex.html',
            {},
            context_instance=RequestContext(request)
        )
    """
def contactform(request):
    if request.user.is_authenticated() and request.user.is_superuser:
        logger.debug ("debug request user %s is authenticated"%request.user.username)
        logger.error ("error request user %s is authenticated"%request.user.username)
    else:
        logger.error ("request user %s is authenticated"%request.user.username)
        c={}
        c.update(csrf(request))
        return render_to_response("login.html",c)
    # Handle file upload
    logger.debug ("contact form")
    if request.method == 'POST':
        logger.debug ("contact form1")
        logger.debug ("contact form1")
        form = ContactForm(request.POST, request.FILES)
        logger.debug (form.is_valid())
        if form.is_valid():
            logger.debug ("contact form2")
            picture1 = request.FILES['picture']
            c_id = request.POST['c_id']
            old_pic1 = request.POST['old_pic']
            last_name1 = request.POST['last_name']
            first_name1 = request.POST['first_name']
            sur_name1 = request.POST['sur_name']
            email1 = request.POST['email']
            emp_id1 = request.POST['emp_id']
            phone1 = request.POST['phone']
            supervisor1 = request.POST['supervisor']
            jobtitle1 = request.POST['title']
            department1 = request.POST['department']
            H_No1 = request.POST['H_No']
            Line_1 = request.POST['Line1']
            street1 = request.POST['street']
            colony1 = request.POST['colony']
            city1 = request.POST['city']
            pin1 = request.POST['pin']
            add1 = Address(H_No=H_No1,Line1=Line_1,street=street1,colony=colony1,city=city1,pin=pin1)
            add1.save()
            pin1 = request.POST['pin']
            sup1 = Supervisor.objects.filter(sup_id=supervisor1)[0]
            job1 = JobTitle.objects.filter(title=jobtitle1)[0]
            dep1 = Department.objects.filter(dep_name=department1)[0]
            logger.debug (c_id)
            logger.debug ("old_pic1 " + str(old_pic1))
            if ((int(c_id) == 0) and (old_pic1 == '0')):
               logger.debug ("new contact saving")
               newdoc = Contact(first_name=first_name1,last_name=last_name1,sur_name=sur_name1,email=email1,emp_id=emp_id1,supervisor=sup1,department=dep1,job_title=job1,phone=phone1,picture=picture1,address=add1)
               newdoc.save()
            elif ((int(c_id) > 0)):
               logger.debug ("edited contact saving")
               con_obj = Contact.objects.get(id=c_id)
               con_obj.first_name = first_name1
               con_obj.last_name = last_name1
               con_obj.sur_name = sur_name1
               con_obj.email = email1
               con_obj.emp_id = emp_id1
               con_obj.supervisor = sup1
               con_obj.department = dep1
               con_obj.job_title = job1
               con_obj.phone = phone1
               con_obj.address = add1
               if picture1 == None:
                  con_obj.picture = old_pic1
               else:
                  con_obj.picture = picture1
               con_obj.save()


            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('modelsapp.views.contactform'))
    else:
        default_data={'c_id':0,'old_pic':'0'}
        form = ContactForm(default_data) # A empty, unbound form

    # Load documents for the list page
    #documents = Document.objects.all()
    supervisors = Supervisor.objects.all()
    jobtitle = JobTitle.objects.all()
    department = Department.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'contactform.html',
        #{'documents': documents, 'form': form},
        {'form': form,'supervisors':supervisors,'jobtitle':jobtitle,'department':department,'user':request.user},
        context_instance=RequestContext(request)
    )#

