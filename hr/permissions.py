from django.contrib.auth.models import Group ,Permission
from rest_framework import permissions
from hr.models import Employee , PositionGroup


class IsSuperUserOrHasGroupPermission(permissions.BasePermission):
    """
    Custom permission class to check if user has allowed group permission or is a superuser
    """

    def has_permission(self, request, view):
        user = request.user
        employee = Employee.objects.get(email=user.email)
        valid = employee.group.filter(method=request.method).exists()
        print(view.action)
        return True
