from django.contrib import admin
from django.contrib.auth.models import Group ,Permission
# Register your models here.
from hr.models import *

admin.site.register(Permission)

admin.site.register(Employee)
admin.site.register(Company)
admin.site.register(PositionGroup)
admin.site.register(doc)
