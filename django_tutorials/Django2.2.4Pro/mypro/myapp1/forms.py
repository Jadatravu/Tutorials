from django.forms import ModelForm
from .models import m_model
class m_form(ModelForm):
    class Meta:
        model = m_model
        fields = ['i_d','description','code']
