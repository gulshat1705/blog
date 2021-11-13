from django import forms
# from django.core.validators import validate_email
from user.models import User


class UserForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ('username', 'password')    