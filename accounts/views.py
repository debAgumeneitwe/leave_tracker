from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import UserLoginForm
from django.views.generic import View
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from .models import Employee
from .forms import UserLoginForm



class UserLoginView(View):
    form_class = UserLoginForm
    template_name = "accounts/login_view.html"

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    #
    # # process data in the form
    # def post(self, request):
    #     form = self.form_class(request.POST)
    #     print(form.data)
    #
    #     if form.is_valid():
    #         print(form.errors)
    #
    #         # cleaned (normalized) data
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #
    #         # user.set_password(password)
    #         # user.save()

    # Logging in
    def login(self, request):
        username = request.POST['username']
        password = request.POST['password']
        print(form.data)
        user = authenticate(request, username=username, password=password)
        if user is not None:

            if user.is_active:
                login(request, user)
                request.user.username
                # Redirect to a success page.
                return redirect('tracker:index')
        else:
            # Return an 'invalid login' error message.
            print(form.errors)

        return render(request, self.template_name, {'form': form})


    #     username = request.POST['username']
    #     password = request.POST['password']
    #
    #     # returns user objects if credentials are correct
    #     user = authenticate(request, username=username, password=password)
    #
    #     if user is not None:
    #         login(request, user)
    #         if user.is_active:
    #             # login(request, user)
    #             # print("succESSFuLL")
    #             # return redirect('trackerApp:trackerApp_page1.html')
    #             return render(request, 'trackerApp/trackerApp_page1.html')
    # else:
    #     print(form.errors)
    #
    # return render(request, self.template_name, {'form': form})
    # print("oooops")

        # def logout_view(request):
        #     logout(request)
        #     # Redirect to a success page.


# @login_required
# @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('settings:profile')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'profiles/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })