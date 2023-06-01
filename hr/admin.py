from django.contrib import admin

# Register your models here.
from hr.models import *

admin.site.register(Employee)
admin.site.register(Compamy)
admin.site.register(Action)
admin.site.register(PositionGroup)
admin.site.register(doc)
