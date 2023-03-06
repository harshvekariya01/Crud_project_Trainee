from django.contrib import admin
from .models import leave,Employee


class Employee1(admin.ModelAdmin):
    list_display = ['username','first_name', 'last_name', 'email','password']
admin.site.register(Employee,Employee1)

class leave1(admin.ModelAdmin):
    list_display = ['user', 'start_date', 'end_date','remaining_leave','reason','approved']
admin.site.register(leave,leave1)