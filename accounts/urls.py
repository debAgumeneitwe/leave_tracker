from django.conf.urls import url
from . import views
from accounts.views import login_view
from django.contrib.auth import authenticate, login

urlpatterns = [
    # url(r'^$', views.UserFormView.as_view(), name='signup'),
    #url(r'^login/$', views.login_view, name='login'),
    url(r'^login/$', views.UserLoginForm.as_view(), name='login'),
    ]