from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from .models import EmployeeProfile

urlpatterns = [url(r'^$', ListView.as_view(
    queryset=EmployeeProfile.objects.all().order_by("employee_id"), template_name="trackerApp/trackerApp_page1.html"),
                   name='home'),
               ]