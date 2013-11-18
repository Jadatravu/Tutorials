# Create your views here.
from django.shortcuts import render
from formapp.form import ContactForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse

def contact(request):
    html = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            html = html + cd['subject'] + cd['email'] + cd['message']
            return HttpResponse(html)
    else:
        form = ContactForm()
    return render(request,'contact_form.html',{'form':form})

