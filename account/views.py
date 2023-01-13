from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, InsertNewPothole
from django.contrib.auth import authenticate, login, logout
from .models import Pothole
from django.db import connection
from django.core.files.storage import FileSystemStorage
# Create your views here.


def index(request):
    return render(request, 'index.html')


def dictfetchall(cursor):
    #"Return all rows from a cursor as a dict"
    desc = cursor.description

    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


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


def insert_pothole(request):
    form = InsertNewPothole(request.POST, request.FILES)
    user = Pothole(request.POST)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            address = form.cleaned_data.get('address')
            remarks = form.cleaned_data.get('remarks')
            date = form.cleaned_data.get('date')
            img = request.FILES['img']
            fss = FileSystemStorage()
            fss.save(img.name, img)
            p = Pothole(address=address, remarks=remarks, date=date, img=img, user=request.user)
            p.save()
            return redirect('user')
    else:
        form = InsertNewPothole()
    return render(request, 'insert_pothole.html', {'form': form, 'msg': msg})


def logout_view(request):
    logout(request)
    return redirect('login_view')


def admin(request):
    return render(request, 'admin.html')


def user(request):
    stmt = "SELECT p_id, address, remarks, date, img FROM account_pothole WHERE user_id=%s" % request.user.id
    cursor = connection.cursor()
    cursor.execute(stmt)
    r = dictfetchall(cursor)
    return render(request, 'user.html', {'data': r})


def contractor(request):
    return render(request, 'contractor.html')


def corporator(request):
    return render(request, 'corporator.html')


def section_officer(request):
    return render(request, 'section_officer.html')
