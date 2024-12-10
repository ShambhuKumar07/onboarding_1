#compliance/admin.py

from django.contrib import admin
from .models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['uan_number', 'pan_number', 'esic_number']
    search_fields = ['uan_number', 'pan_number', 'esic_number']


####################### Add compliance data in profile

# Define an inline for Employee (compliance)
class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 1

admin.site.register(Employee, EmployeeAdmin)
