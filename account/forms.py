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


class CorpRegForm(UserCreationForm):
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


class InsertNewPotholeForm(forms.ModelForm):

    class Meta:
        model = Pothole
        fields = ('p_id', 'address', 'remarks', 'date', 'img', 'ward_no')
        exclude = ['user']


class UpdatePotholeForm(forms.ModelForm):

    class Meta:
        model = Pothole
        fields = ('p_id', 'address', 'remarks', 'date', 'img', 'ward_no')
        exclude = ['user']
    
    def __init__(self, *args, **kwargs):
        super(UpdatePotholeForm, self).__init__(*args, **kwargs)
        self.fields['address'].required = False
        self.fields['remarks'].required = False
        self.fields['date'].required = False
        self.fields['img'].required = False
        self.fields['ward_no'].required = False


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


class AssignPotholeForm(forms.ModelForm):
    
    class Meta:
        model = Allotment
        fields = ('p_id', 'c_id')


class ContMarkDoneForm(forms.ModelForm):

    class Meta:
        model = Pothole
        fields = ('p_id',)
        exclude = ['address', 'remarks', 'date', 'img', 'user_id', 'ward_no', 'cont_done', 'corp_done']


class CorpMarkDoneForm(forms.ModelForm):

    class Meta:
        model = Pothole
        fields = ('p_id',)
        exclude = ['address', 'remarks', 'date', 'img', 'user_id', 'ward_no', 'cont_done', 'corp_done']