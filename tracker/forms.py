"""User Registration"""
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # making the password hidden

    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # fields appearing on the form