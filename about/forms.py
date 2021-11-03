from django import forms
from django.core.exceptions import ValidationError
# from django.db import models
# from django.forms import widgets
from about.models import About 
# from django.core import validators


# class AboutForm(forms.Form):
#     email = forms.EmailField(error_messages={'required': 'Error! Enter your email with @!'})
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     message = forms.CharField(max_length=200)
#     allow_mailing = forms.BooleanField()

class AboutForm(forms.ModelForm):
    class Meta: 
        model = About
        fields = '__all__'

    def cleaned_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@gmail.com'):
            raise ValidationError('ERROR! Wrong email!')
        return email    
