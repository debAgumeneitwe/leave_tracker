from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from trackerApp.models import Employee

urlpatterns = [url(r'^$', ListView.as_view(queryset=Employee.objects.all().order_by("employee_id"), template_name="trackerApp/trackerApp_page1.html")),
               ]