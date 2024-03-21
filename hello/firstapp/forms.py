from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Post

class Reg_User_Form(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Логин'}))
    email = forms.CharField(label="Email", widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Email'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label="Пароль (повтор)", widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Пароль (повторно)'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class Auth_User_Form(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Логин'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')
