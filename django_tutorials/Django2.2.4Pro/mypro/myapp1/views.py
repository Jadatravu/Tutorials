from django.shortcuts import render

from django.shortcuts import render_to_response
from .forms import m_form
# Create your views here.

def form_view(request):
    if request.method == 'POST':
        form = m_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = m_form()
    return render_to_response('m.html',{'form':form})
