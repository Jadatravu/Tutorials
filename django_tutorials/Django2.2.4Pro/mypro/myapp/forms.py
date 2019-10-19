from django.forms import ModelForm
from .models import mymodel, student

class mform(ModelForm):
    class Meta:
        model = mymodel
        fields = ['index','description','code']

class sform(ModelForm):
    class Meta:
        model = student
        fields = ['name','c_lass','tea','pri']
