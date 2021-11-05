from django import forms
from django.core.exceptions import ValidationError
from about.models import About 



class AboutForm(forms.ModelForm):
    class Meta: 
        model = About
        fields = '__all__'