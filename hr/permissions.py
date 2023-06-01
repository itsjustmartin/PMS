from django.contrib.auth.models import Group
from rest_framework import permissions
from hr.models import Action, Employee



class IsSuperUserOrHasGroupPermission(permissions.BasePermission):
    """
    Custom permission class to check if user has allowed group permission or is a superuser
    """

    def has_permission(self, request, view):
        user = request.user
        employee = Employee.objects.get(email=user.email)
        group= employee.group
        print(group)
        print(group.action)
        print(view.action)
        return True
        # required_groups = view.permission_groups.get(view.action)

        # # Return False if no permission groups are found
        # if not required_groups:
        #     return False

        # # Get user's groups if authenticated else set it to empty list
        # user_groups = (
        #     request.user.groups.values_list('name', flat=True)
        #     if request.user.is_authenticated
        #     else []
        # )

        # # Check if any of the required groups are present in user's groups
        # is_allowed_group = [(group in user_groups) for group in required_groups]

        # # Check if user is a superuser or any of the required groups are present in user's groups
        # is_allowed = (
        #     'SuperUser' in user_groups or
        #     any(is_allowed_group)
        # )
        # return is_allowed