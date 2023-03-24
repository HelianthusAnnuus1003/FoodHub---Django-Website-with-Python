from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInputUsername', 'placeholder': 'myusername', 'required': 'true', 'autofocus': 'true', 'type': 'text'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInputEmail', 'placeholder': 'email', 'required': 'true', 'type': 'email'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingPassword', 'placeholder': 'paswword', 'required': 'true', 'type': 'password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingPasswordConfirm', 'placeholder': 'paswword confim', 'required': 'true', 'type': 'password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


