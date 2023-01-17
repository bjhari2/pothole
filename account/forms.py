from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Pothole, Corporator, Contractor, Allotment


class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class CorporatorRegistration(UserCreationForm):
    ward_list = Corporator.objects.all()
    ward_no = forms.ModelChoiceField(
        queryset=ward_list,
        widget=forms.Select()
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('ward_no', 'email', 'password1', 'password2')
        exclude = ['username', 'is_user', 'is_contractor', 'is_corporator']


class InsertNewPothole(forms.ModelForm):

    class Meta:
        model = Pothole
        fields = ('p_id', 'address', 'remarks', 'date', 'img', 'ward_no')
        exclude = ['user']


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_user', 'is_contractor')


class AssignToContractor(forms.ModelForm):
    query1 = Pothole.objects.all()
    query2  = Contractor.objects.all()
    p_id = forms.ModelChoiceField(
        queryset=query1,
        widget=forms.Select()
    )
    c_id = forms.ModelChoiceField(
        queryset=query2,
        widget=forms.Select()
    )

    class Meta:
        model = Allotment
        fields = ('p_id', 'c_id')