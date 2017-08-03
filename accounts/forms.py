"""User Registration and login"""
from django.contrib.auth.models import User
from django import forms


class UserLoginForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)  # making the password hidden

    class Meta:
        model = User
        fields = ['username', 'Password']

