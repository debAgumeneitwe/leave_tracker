from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class EmployeeProfile(models.Model):
    DTS = 'DTS'
    DEGS = 'DEGS'
    DFA = 'DFA'
    DPRD = 'DPRD'
    LEGAL = 'LEGAL'
    DEPARTMENT_CHOICES = (
        (DTS, 'D.Technical Services'),
        (DEGS, 'D. E-Govt'),
        (DFA, 'D. Finance and Admin'),
        (DPRD, 'Planning'),
        (LEGAL, 'Legal')
    )
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=10)
    employee_name = models.CharField(max_length=50)
    position = models.CharField(max_length=25)
    department = models.CharField(
        max_length=5,
        choices=DEPARTMENT_CHOICES,
        default=DFA,
    )
    start_date = models.DateField(null=True, blank=True)

    # creating a profile; linking profile to user
    def create_profile(sender, **kwargs):
        if kwargs['created']:
            employee_profile = EmployeeProfile.objects.create(username=kwargs['instance'])

    post_save.connect(create_profile, sender=User)

    # def __str__(self):
    #     return self.employee_name

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         EmployeeProfile.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()
