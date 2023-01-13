from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Pothole


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


class InsertNewPothole(forms.Form):
    address = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class" : "form-control"
            }
        )
    )
    remarks = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    date = forms.DateField(
        widget= forms.DateInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = Pothole
        fields = ('p_id', 'address', 'remarks', 'date', 'img', 'user')


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
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_user', 'is_contractor', 'is_corporator', 'is_section_officer')