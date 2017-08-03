from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import UserLoginForm
from django.views.generic import View
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Employee
from .forms import UserLoginForm



"""def login_view(request):
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data.get["username"]
        password = form.cleaned_data.get("password")

    return render(request, "login_view.html", {"form": form})


    #return user objects if credentials are correct
    user = authenticate(username=username, password=password)

def request_view(request):
    return render(request, "form.html", {})

def logout_view(request):
    return render(request, "form.html", {})"""

class UserLoginView(View):
    form_class = UserLoginForm
    template_name = "accounts/login_view.html"

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #process data in the form
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('tracker:index')

        return render(request, self.template_name, {'form':form})