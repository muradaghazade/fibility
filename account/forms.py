from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from .models import User
from django_range_slider.fields import RangeSliderField


class AdvisorRegisterForm(UserCreationForm):
    # salary = RangeSliderField(minimum=0,maximum=100000,step=1)

    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'password',
                'class' : 'form-control',
            }))

    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'confirm password',
                'class' : 'form-control',
            }))
        
    profile_pic = forms.FileField(
        widget = forms.FileInput(
            attrs={
                'id': "pic"
            }))

    class Meta:
        model = User
        fields = ('username','full_name','email','password1','password2','occupation', 'salary', 'number', 'company', 'is_advisor', 'profile_pic')

        widgets = {
            'full_name': forms.TextInput(attrs={'id': 'fullname', 'placeholder': 'Full Name', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'id': 'username', 'placeholder': 'Username', 'class': 'form-control'}),
            # 'region': forms.TextInput(attrs={'id': 'username', 'placeholder': 'Username', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'placeholder': 'name@gmail.com', 'class': 'form-control'}),
            'is_employed': forms.CheckboxInput(attrs={'id': 'is_employed'}),
            'is_advisor': forms.CheckboxInput(attrs={'id': 'is_advisor', 'checked':'True'}),
            'occupation': forms.TextInput(attrs={'id': 'occupation', 'placeholder': 'occupation', 'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'id': 'number', 'placeholder': '012 345 678 910', 'class': 'form-control', 'pattern': '[0-9]{3}-[0-9]{2}-[0-9]{3}'}),
            'salary': forms.NumberInput(attrs={'type': 'range', 'min':'0', 'max': '100000','id': 'myRange', 'placeholder': 'salary', 'class': 'form-inputs'}),
            'company': forms.TextInput(attrs={'id': 'company', 'placeholder': 'company', 'class': 'form-control'}),
        }

class SeekerRegisterForm(UserCreationForm):
    # salary = RangeSliderField(minimum=0,maximum=100000,step=1)

    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'password',
                'class' : 'form-control',
            }))

    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'confirm password',
                'class' : 'form-control',
            }))
        
    profile_pic = forms.FileField(
        widget = forms.FileInput(
            attrs={
                'id': "pic"
            }))

    class Meta:
        model = User
        fields = ('username','full_name','email','password1','password2', 'is_employed', 'occupation', 'salary', 'number', 'is_seeker', 'profile_pic', 'age')

        widgets = {
            'full_name': forms.TextInput(attrs={'id': 'fullname', 'placeholder': 'Full Name', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'id': 'username', 'placeholder': 'Username', 'class': 'form-control'}),
            # 'region': forms.TextInput(attrs={'id': 'username', 'placeholder': 'Username', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'placeholder': 'name@gmail.com', 'class': 'form-control'}),
            'is_employed': forms.CheckboxInput(attrs={'id': 'radio-yes', 'type': 'radio'}),
            'is_seeker': forms.CheckboxInput(attrs={'id': 'is_seeker', 'checked': 'True'}),
            'age': forms.NumberInput(attrs={'id': 'number', 'placeholder': 'Age', 'class': 'form-control'}),
            'occupation': forms.TextInput(attrs={'id': 'occupation', 'placeholder': 'occupation', 'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'id': 'number', 'placeholder': '012 345 678 910', 'class': 'form-control', 'pattern': '[0-9]{3}-[0-9]{2}-[0-9]{3}'}),
            'salary': forms.NumberInput(attrs={'type': 'range', 'min':'0', 'max': '100000','id': 'myRange', 'placeholder': 'salary', 'class': 'form-inputs'}),
            # 'company': forms.TextInput(attrs={'id': 'company', 'placeholder': 'company', 'class': 'form-control'}),
        }

class LoginForm(AuthenticationForm):
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Password',
                'class' : 'form-control',
            }))

    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'id': 'username',
                'placeholder': 'Your Username',
                'class': 'form-control'
            }))

    email = forms.CharField(
        widget = forms.EmailInput(
            attrs={
                'id': 'email',
                'placeholder': 'Your Email',
                'class': 'form-control'
            }))

    class Meta:
        model = User
        fields = ['email', 'password']
