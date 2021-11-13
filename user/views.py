from django.shortcuts import render, redirect
from django.http.response import HttpResponseBadRequest
from user.forms import UserForm
from user.personal_info.forms import PersonalInfoForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return redirect('home')
        else:
            raise HttpResponseBadRequest
    else:
        raise HttpResponseBadRequest


def logout(request):
    django_logout(request)
    return redirect('home')        


def registration(request):
    if request.method == 'GET':
        return render(request, 'registration.html')
    elif request.method == 'POST':
        user_data = UserForm(request.POST)
        personal_info_data = PersonalInfoForm(request.POST)
        if user_data.is_valid() and personal_info_data.is_valid():
            personal_info_instance = personal_info_data.save()
            user_instance = user_data.save(False)
            user_instance.personal_info = personal_info_instance
            user_instance.set_password(user_data.cleaned_data['password'])
            user_instance.save()
            print('user_data is valid and saved')

        #save data, store token and redirect to main page
        return redirect('home')        