# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 06:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trackerApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=10)),
                ('employee_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=25)),
                ('department', models.CharField(choices=[('DTS', 'D.Technical Services'), ('DEGS', 'D. E-Govt'), ('DFA', 'D. Finance and Admin'), ('DPRD', 'Planning'), ('LEGAL', 'Legal')], default='DFA', max_length=5)),
                ('start_date', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
