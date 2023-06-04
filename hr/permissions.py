from django.contrib.auth.models import Group
from rest_framework import permissions
from hr.models import Action, Employee , PositionGroup



class IsSuperUserOrHasGroupPermission(permissions.BasePermission):
    """
    Custom permission class to check if user has allowed group permission or is a superuser
    """

    def has_permission(self, request, view):
        user = request.user
        employee = Employee.objects.get(email=user.email)
        valid = employee.group.action.filter(name=view.action).exists()
        return valid
