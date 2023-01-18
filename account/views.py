from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, InsertNewPotholeForm, CorpRegForm, AssignPotholeForm
from django.contrib.auth import authenticate, login, logout
from .models import User, Pothole, Corporator, Contractor
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
            user = form.save(commit=False)
            user.save()
            if user.is_contractor:          # Populating Contractor table if user is a Contractor
                c_obj = Contractor(c_id=user.id, name=user.username)
                c_obj.save()
            msg = 'User created'
            return redirect('login_view')
        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})


#Corporator Registration view
def corp_register(request):
    msg = None
    name = None
    ward_list = Corporator.objects.all()
    if request.method == 'POST':
        form = CorpRegForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            # Select name from corporator where ward_no = request.POST['ward_no']
            name = Corporator.objects.filter(ward_no=request.POST['ward_no']).values('name')
            p.username = name                           # Setting user name for Corporator from Corporator table value
            p.is_corporator = True                      # Setting is_corporator field to True before committing
            p.save()
            msg = 'User created'
            return redirect('login_view')
        else:
            msg = 'Form is not valid'
            print(form.errors.as_data())
    else:
        form = SignUpForm()
    return render(request, 'corporator_register.html', {'form': form, 'ward_list': ward_list ,'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_user:
                login(request, user)
                return redirect('user')
            elif user is not None and user.is_contractor:
                login(request, user)
                return redirect('contractor')
            elif user is not None and user.is_corporator:
                login(request, user)
                return redirect('corporator')
            else:
                msg = 'Invalid Credentials. Please Try Again'
        else:
            msg = 'Error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def logout_view(request):
    logout(request)
    return redirect('login_view')


#Inserting new pothole repair request by user
def insert_pothole(request):
    form = InsertNewPotholeForm(request.POST, request.FILES)
    ward_list = Corporator.objects.values('ward_no')
    if request.method == 'POST':
        if form.is_valid():
            p = form.save(commit=False)
            p.user = User.objects.get(id=request.user.id)               # Setting user id as id of the currently logged in user
            p.save()
            return redirect('user')
    else:
        form = InsertNewPotholeForm()
    return render(request, 'insert_pothole.html', {'form': form, 'ward_list': ward_list})


def assign_pothole(request):
    data = Pothole.objects.filter(ward_no = request.user.ward_no)
    form = AssignPotholeForm(request.POST or None)
    p_list = Pothole.objects.filter(ward_no = request.user.ward_no)
    c_list  = Contractor.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            alltoment = form.save(commit=False)
            alltoment.p_id = request.POST['p_id']
            alltoment.c_id = request.POST['c_id']
            alltoment.save()
            return redirect('corporator')
    else:
        form = AssignPotholeForm()
    return render(request, 'assign_pothole.html', {'form': form, 'data': data, 'p_list': p_list, 'c_list': c_list})

#User page view
def user(request):
    r = Pothole.objects.filter(user_id = request.user.id)
    data = {'data' : r}
    return render(request, 'user.html', data)


#Contractor page view
def contractor(request):
    return render(request, 'contractor.html')


#Corporator page view
def corporator(request):
    r = Pothole.objects.filter(ward_no = request.user.ward_no)
    data = {'data' : r}
    return render(request, 'corporator.html', data)

