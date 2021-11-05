from django.shortcuts import render
from about.forms import AboutForm
from about.models import About
from django.core.exceptions import ValidationError
from django.contrib import messages


def about(request):
    if request.method == 'POST':
        data_form =AboutForm(request.POST)
        if data_form.is_valid():
            email = data_form.cleaned_data['email']
            first_name = data_form.cleaned_data['first_name']
            last_name = data_form.cleaned_data['last_name']
            message = data_form.cleaned_data['message']
            allow_mailing = data_form.cleaned_data['allow_mailing']
            about_object = About(email=email, first_name=first_name, last_name=last_name,message=message, allow_mailing=allow_mailing)          
            about_object.save()
            print('Saved')

            messages.success(request, f'{first_name}, your message was sent!')        
       
    form = AboutForm()
    about_data = About.objects.all() #select *from about
    # About.objects.delete() #delete from about
    return render(request, "about.html", {'title': 'About', 'form': form, 'data': about_data}) 