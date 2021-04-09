from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm,UsernameField
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
                'id': "nopic"
            }), required=False)

    class Meta:
        model = User
        fields = ('full_name','email','password1','password2','occupation', 'salary', 'number', 'is_advisor', 'profile_pic', 'state', 'start_budget', 'end_budget')

        widgets = {
            'full_name': forms.TextInput(attrs={'id': 'fullname', 'placeholder': 'Full Name', 'class': 'form-control'}),
            'state': forms.Select(attrs={'id': 'sell', 'class': 'form-control select__field'}),
            'start_budget': forms.Select(attrs={'id': 'start-budget', 'class': 'form-control select__field'}),
            'end_budget': forms.Select(attrs={'id': 'end-budget', 'class': 'form-control select__field'}),
            # 'type_of_advice': forms.Select(attrs={'id': 'sell', 'class': 'form-control select__field'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'placeholder': 'name@gmail.com', 'class': 'form-control'}),
            'is_employed': forms.CheckboxInput(attrs={'id': 'is_employed'}),
            'is_advisor': forms.CheckboxInput(attrs={'id': 'is_advisor', 'checked':'True'}),
            'occupation': forms.TextInput(attrs={'id': 'occupation', 'placeholder': 'occupation', 'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'id': 'phone', 'placeholder': '012-345-6789', 'class': 'form-control', 'pattern': '[0-9]{3}-[0-9]{2}-[0-9]{3}'}),
            'salary': forms.NumberInput(attrs={'id': 'salary', 'placeholder': 'Salary', 'class': 'form-control'}),
            # 'company': forms.TextInput(attrs={'id': 'company', 'placeholder': 'company', 'class': 'form-control'}),
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

    class Meta:
        model = User
        fields = ('full_name','email','password1','password2', 'occupation', 'salary', 'number', 'is_seeker', 'profile_pic', 'age', 'state', 'start_budget', 'end_budget')

        widgets = {
            'full_name': forms.TextInput(attrs={'id': 'fullname', 'placeholder': 'Full Name', 'class': 'form-control'}),
            'state': forms.Select(attrs={'id': 'sell', 'placeholder': 'Username', 'class': 'form-control select__field'}),
            'start_budget': forms.Select(attrs={'id': 'start-budget', 'class': 'form-control select__field'}),
            'end_budget': forms.Select(attrs={'id': 'end-budget', 'class': 'form-control select__field'}),
            # 'type_of_advice': forms.Select(attrs={'id': 'sell', 'class': 'form-control select__field'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'placeholder': 'name@gmail.com', 'class': 'form-control'}),
            'is_seeker': forms.CheckboxInput(attrs={'id': 'is_seeker', 'checked': 'True'}),
            'age': forms.NumberInput(attrs={'id': 'number', 'placeholder': 'Age', 'class': 'form-control'}),
            'occupation': forms.TextInput(attrs={'id': 'occupation', 'placeholder': 'occupation', 'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'id': 'phone', 'placeholder': '123-456-7890', 'class': 'form-control', 'pattern': '[0-9]{3}-[0-9]{2}-[0-9]{3}'}),
            'salary': forms.NumberInput(attrs={'id': 'salary', 'placeholder': 'Salary range', 'class': 'form-control'}),
            # 'company': forms.TextInput(attrs={'id': 'company', 'placeholder': 'company', 'class': 'form-control'}),
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': True,
        'class': 'form-control',
        'placeholder': 'Email',
        'name': 'email'
    }))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'class': 'form-control',
            'name': 'password',
            'placeholder': 'Password'
        }),
    )

    class Meta:
        model = User
        fields = ['username', 'password']


class UpdateProfileForm(forms.ModelForm):

    profile_pic = forms.FileField(
        widget = forms.FileInput(
            attrs={
                'id': "nopic"
            }), required=False)

    class Meta:
        model = User
        fields = ['full_name', 'email', 'number', 'profile_pic', 'state', 'start_budget', 'end_budget', 'salary']

        widgets = {
            'full_name': forms.TextInput(attrs={'id': 'full_name', 'placeholder': 'First Name',  'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'placeholder': 'Bio',  'class': 'form-control'}),
            'state': forms.Select(attrs={'id': 'sell', 'placeholder': 'Username', 'class': 'form-control select__field'}),
            'start_budget': forms.Select(attrs={'id': 'start-budget', 'class': 'form-control select__field'}),
            'end_budget': forms.Select(attrs={'id': 'end-budget', 'class': 'form-control select__field'}),
            'salary': forms.NumberInput(attrs={'id': 'salary', 'placeholder': 'Budget', 'class': 'form-control'}),
            # 'company': forms.TextInput(attrs={'id': 'company', 'placeholder': 'company', 'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'id': 'phone', 'placeholder': '123-456-7890', 'class': 'form-control', 'pattern': '[0-9]{3}-[0-9]{2}-[0-9]{3}'}),
        }
