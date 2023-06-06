from django.db import models
from django.conf import settings

import datetime
from django.utils import timezone

from django.contrib.auth.models import Group, Permission
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
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )


class Auditable(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="usersAddedByme",
        null=True,
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        db_index=True,  # db_index for faster lookup
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="usersUpdatedByme",
        on_delete=models.SET_NULL,
        null=True,
    )
    updated_at = models.DateTimeField(auto_now=True)


class Employee(Auditable):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.ForeignKey(
        Company,
        related_name='company_employee_set',
        on_delete=models.CASCADE,
    )
    group = models.ForeignKey(
        PositionGroup,
        related_name='employee_set',
        related_query_name='employee',
        on_delete=models.CASCADE,
    )
    salary = models.PositiveIntegerField()

    def is_joined_new(self):
        return self.created_on >= timezone.now() - datetime.timedelta(days=90)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class doc(models.Model):
    name = models.CharField(max_length=30)
