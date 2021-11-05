from django import forms
# from django.core.validators import validate_email
from about.models import About 


class AboutForm(forms.ModelForm):
    class Meta: 
        model = About
        fields = '__all__'    