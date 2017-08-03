from django.db import models

class Employee(models.Model):
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
    employee_id = models.CharField(max_length=10)
    employee_name = models.CharField(max_length=50)
    position = models.CharField(max_length=25)
    department = models.CharField(
        max_length=5,
        choices=DEPARTMENT_CHOICES,
        default=DFA,
    )
    start_date = models.DateTimeField()

    def __str__(self):
        return self.employee_name
