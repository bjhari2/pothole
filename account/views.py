from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, InsertNewPotholeForm, UpdatePotholeForm, CorpRegForm, AssignPotholeForm, ContMarkDoneForm, CorpMarkDoneForm
from django.contrib.auth import authenticate, login, logout
from .models import User, Pothole, Corporator, Contractor, Allotment, Done
# Create your views here.


def index(request):
    return render(request, 'index.html')


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
    return render(request, 'ins_updt_pothole.html', {'form': form, 'ward_list': ward_list, 'update': False})


#Updating pothole details by user
def update_pothole(request):
    data_pending = Pothole.objects.filter(user_id = request.user.id, corp_done = False)
    edit = Pothole.objects.get(p_id = request.GET['p_id'])
    form = UpdatePotholeForm(request.POST or None, instance=edit)
    ward_list = Corporator.objects.values('ward_no')
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('user')
    else:
        form = UpdatePotholeForm()
    return render(request, 'ins_updt_pothole.html', {'form': form, 'edit':edit, 'data_pending':data_pending, 'ward_list': ward_list, 'update': True})


#View to assign pothole to a contractor
def assign_pothole(request):
    form = AssignPotholeForm(request.POST or None)
    data = Pothole.objects.filter(ward_no = request.user.ward_no.ward_no)
    p_list = Pothole.objects.filter(ward_no = request.user.ward_no.ward_no).exclude(p_id__in=Allotment.objects.all())
    c_list  = Contractor.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('corporator')
    else:
        form = AssignPotholeForm()
    return render(request, 'assign_pothole.html', {'form': form, 'data': data, 'p_list': p_list, 'c_list': c_list})


#View to mark pothole repair request as done by contractor
def cont_mark_done(request):
    form = ContMarkDoneForm(request.POST or None)
    data = Pothole.objects.filter(allotment__c_id = request.user.id)
    p_list = Pothole.objects.filter(allotment__c_id = request.user.id, cont_done = False)
    if request.method == 'POST':
        if form.is_valid():
            update = Pothole.objects.get(p_id=request.POST['p_id'])
            update.cont_done = True
            update.save()
            return redirect('contractor')
    else:
        form = ContMarkDoneForm()
    return render(request, 'cont_mark_done.html', {'p_list': p_list, 'data': data})


#View to mark pothole repair request as done by contractor
def corp_mark_done(request):
    form = CorpMarkDoneForm(request.POST or None)
    data = Pothole.objects.filter(ward_no = request.user.ward_no, cont_done = True, corp_done = False)
    p_list = Pothole.objects.filter(ward_no = request.user.ward_no, cont_done = True, corp_done = False)
    if request.method == 'POST':
        if form.is_valid():
            update = Pothole.objects.get(p_id=request.POST['p_id'])
            update.corp_done = True
            done = Done.objects.create(p_id=Pothole.objects.get(p_id=request.POST['p_id']).p_id,
                    address=Pothole.objects.get(p_id=request.POST['p_id']).address,
                    remarks=Pothole.objects.get(p_id=request.POST['p_id']).remarks,
                    date=Pothole.objects.get(p_id=request.POST['p_id']).date,
                    img=Pothole.objects.get(p_id=request.POST['p_id']).img,
                    user=User.objects.get(pothole__p_id=request.POST['p_id']),
                    ward_no=Corporator.objects.get(user__ward_no=request.user.ward_no.ward_no)
            )
            done.save()
            update.delete()
            return redirect('corporator')
    else:
        form = CorpMarkDoneForm()
    return render(request, 'corp_mark_done.html', {'p_list': p_list, 'data': data})


#User page view
def user(request):
    data_done = Done.objects.filter(user_id = request.user.id)
    data_pending = Pothole.objects.filter(user_id = request.user.id, corp_done = False)
    return render(request, 'user.html', {'data_pending': data_pending, 'data_done': data_done})


#Contractor page view
def contractor(request):
    #SELECT p.p_id, address, remarks, date, img, user_id, ward_no FROM account_pothole p INNER JOIN account_allotment a ON (p.p_id = a.p_id) WHERE a.c_id = request.user.id
    data_done = Pothole.objects.filter(allotment__c_id = request.user.id, cont_done = True)
    data_pending = Pothole.objects.filter(allotment__c_id = request.user.id, cont_done = False)
    return render(request, 'contractor.html', {'data_done': data_done, 'data_pending': data_pending})


#Corporator page view
def corporator(request):
    data_done = Pothole.objects.filter(ward_no = request.user.ward_no, cont_done = True)
    data_pending = Pothole.objects.filter(ward_no = request.user.ward_no, cont_done = False)
    return render(request, 'corporator.html', {'data_done': data_done, 'data_pending': data_pending})

