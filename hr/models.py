from django.db import models

from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission, UserManager
from django.utils.translation import gettext_lazy as _


class Compamy(models.Model):
    name = models.CharField(max_length=50, unique=True)
    field = models.CharField(max_length=50,)


class Action(models.Model):
    name =models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class PositionGroup(Group):
    # name 
    # permisions
    action = models.ManyToManyField(
        Action,
        related_name="actoin_position_set",
    )
    managed_by = models.ForeignKey(
        'self',
        # 'hr.models.PositionGroup',
        # related_name="managing_group_set",
        on_delete= models.CASCADE,
        null=True,
        blank=True,
        )
    
    
class EmployeeManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        print(user.password)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)
    
    # def create_superuser(self, email, password, **extra_fields):
    #     extra_fields.setdefault("is_staff", True)
    #     extra_fields.setdefault("is_superuser", True)

    #     if extra_fields.get("is_staff") is not True:
    #         raise ValueError("Superuser must have is_staff=True.")
    #     if extra_fields.get("is_superuser") is not True:
    #         raise ValueError("Superuser must have is_superuser=True.")

    #     return self._create_user(email, password, **extra_fields)   



class Employee(AbstractUser):
    username = None
    email = models.EmailField(
        _("email address"),
        unique=True,
    )
    company = models.ForeignKey(
        Compamy,
        related_name="company_employee_set",
        on_delete= models.CASCADE,
    )
    group = models.ForeignKey(
        PositionGroup,
        related_name="employee_set",
        related_query_name="employee",
        on_delete= models.CASCADE,
    )
    groups= None
    user_permissions = None

    salary = models.IntegerField(default=100)
    objects = EmployeeManager()
    # position_group = 
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    


class doc(models.Model):
    name =models.CharField(max_length=30)
