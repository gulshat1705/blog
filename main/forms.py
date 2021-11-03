from django import forms
from django.db import models
from models import About 


# class AboutForm(forms.Form):
#     email = forms.EmailField()
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     message = forms.CharField(max_length=200)
#     allow_mailing = forms.BooleanField()

class AboutForm(forms.ModelForm):
    class Meta: 
        model = About
        fields = '__all__'
