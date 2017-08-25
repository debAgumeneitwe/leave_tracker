"""User Registration and login"""
from django.contrib.auth.models import User
from django import forms


class UserLoginForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)  # making the password hidden

    class Meta:
        model = User
        fields = ['username', 'password']  # fields appearing on the form


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')
#
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('url', 'location', 'company')


