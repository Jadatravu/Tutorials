# -*- coding: utf-8 -*-
from django import forms

class ESearchForm(forms.Form):
    search_key=forms.CharField(help_text ='max.30 characters')

class JobTitleForm(forms.Form):
    title=forms.CharField(help_text ='max.30 characters')

class DepartmentForm(forms.Form):
    dep_name=forms.CharField(help_text ='max.30 characters')

class SupervisorForm(forms.Form):
    sup_id=forms.IntegerField()

class ViewContactForm(forms.Form):
    con_id=forms.IntegerField()

class ContactForm(forms.Form):
    picture = forms.FileField(
        label='Contact Picture',
        help_text='max. 42 megabytes'
    )
    c_id=forms.IntegerField(required=False)
    old_pic=forms.CharField(required=False)
    first_name=forms.CharField(help_text ='max.30 characters')
    last_name=forms.CharField(help_text ='max.30 characters')
    sur_name=forms.CharField(help_text ='max.30 characters')
    email=forms.EmailField(help_text ='max.30 characters')
    emp_id=forms.IntegerField()
    phone=forms.IntegerField()
    H_No = forms.CharField()
    Line1 = forms.CharField()
    street = forms.CharField()
    colony = forms.CharField()
    city = forms.CharField()
    pin = forms.IntegerField()
    
   

