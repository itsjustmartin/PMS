from django.db import models
from django.contrib.auth.models import  Group, Permission
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    field = models.CharField(max_length=50,)

class MethodsMap(models.Model):
    name = models.CharField(max_length=20,)

class PositionGroup(Group):
    # name
    # permissions
    method_permissions = models.ManyToManyField(
        MethodsMap,
        blank=True,
    )
    managed_by = models.ForeignKey(
        'self',
        # 'hr.models.PositionGroup',
        # related_name='managing_group_set",
        on_delete= models.CASCADE,
        null=True,
        blank=True,
        )

class Employee(models.Model):
    company = models.ForeignKey(
        Company,
        related_name='company_employee_set',
        on_delete= models.CASCADE,
    )
    group = models.ForeignKey(
        PositionGroup,
        related_name='employee_set',
        related_query_name='employee',
        on_delete= models.CASCADE,
    )
    salary = models.PositiveIntegerField()

    def __str__(self):
        return 


class doc(models.Model):
    name =models.CharField(max_length=30)
