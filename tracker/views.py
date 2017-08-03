# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views import generic
from .forms import UserForm
from django.shortcuts import render, redirect


def index(request):
    # return HttpResponse("<h2>WELCOME TO THE LEAVE TRACKER HOMEPAGE</h2>")
    return render(request, 'tracker/home.html')

def contact(request):
    return render(request, 'tracker/contact.html', {'contents': ['If you have any issues please contact me at','agugudebz@gmail.com']})

"""
class UserFormView(View):
    form_class = UserForm
    template_name = "tracker/signup_form.html"

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process data in the form
    # def post(self, request):
    #     form = self.form_class(request.POST)
    #
    #     if form.is_valid():
    #
    #         user = form.save(commit=False)
    #
    #         # cleaned (normalized) data
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         user.set_password(password)
    #         user.save()
    #
    #         # returns user objects if credentials are correct
    #         user = authenticate(username=username, password=password)
    #
    #         if user is not None:
    #             if user.is_active:
    #                 login(request, user)
    #                 return redirect('tracker:index')"""

