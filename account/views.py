from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, InsertNewPothole
from django.contrib.auth import authenticate, login, logout
from .models import Pothole
from django.db import connection
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_user:
                login(request, user)
                return redirect('user')
            elif user is not None and user.is_contractor:
                login(request, user)
                return redirect('contractor')
            elif user is not None and user.is_corporator:
                login(request, user)
                return redirect('corporator')
            elif user is not None and user.is_section_officer:
                login(request, user)
                return redirect('section_officer')
            else:
                msg = 'Invalid Credentials. Please Try Again'
        else:
            msg = 'Error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def logout_view(request):
    logout(request)
    return redirect('login_view')


def admin(request):
    return render(request, 'admin.html')


def user(request):
    form = InsertNewPothole(request.POST, request.FILES)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            address = form.cleaned_data.get('address')
            remarks = form.cleaned_data.get('remarks')
            date = form.cleaned_data.get('date')
            img = form.cleaned_data.get('img')
            p = Pothole(address=address, remarks=remarks, date=date, img=img)
            p.save()
            return render(request, 'user.html', {'form': form, 'msg': msg})
    else:
        form = InsertNewPothole()
    return render(request, 'user.html', {'form': form, 'msg': msg})


def contractor(request):
    return render(request, 'contractor.html')


def corporator(request):
    return render(request, 'corporator.html')


def section_officer(request):
    return render(request, 'section_officer.html')
