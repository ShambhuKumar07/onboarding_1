#users/admin.py

from django.contrib import admin
from .models import CustomUser, Profile, FamilyMember, EducationalQualification, EmploymentRecord, LanguageProficiency, Reference
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from compliance.models import Employee  # Import the Employee model
from compliance.admin import EmployeeInline
from compensation.models import EmployeeCTC
from import_export.admin import ImportExportModelAdmin


# Register the inlines
class FamilyMemberInline(admin.TabularInline):
    model = FamilyMember
    extra = 1  # Number of extra forms to show (you can adjust this)

class EducationalQualificationInline(admin.TabularInline):
    model = EducationalQualification
    extra = 1

class EmploymentRecordInline(admin.TabularInline):
    model = EmploymentRecord
    extra = 1

class LanguageProficiencyInline(admin.TabularInline):
    model = LanguageProficiency
    extra = 1

class ReferenceInline(admin.TabularInline):
    model = Reference
    extra = 1

class EmployeeCTCInline(admin.TabularInline):

    model=EmployeeCTC
    extra=1


# Admin for Profile
class ProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = [FamilyMemberInline, EducationalQualificationInline, EmploymentRecordInline, LanguageProficiencyInline, ReferenceInline,EmployeeInline,EmployeeCTCInline]
    list_display = ('user', 'Employee_Code', 'first_name', 'last_name')
    search_fields = ('user__username', 'first_name', 'last_name', 'Employee_Code')
     
# Inline Profile for CustomUser
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email')
    ordering = ('username',)

# admin.site.register(CustomUser, CustomUserAdmin)

# Register the CustomUser and Profile models with the admin
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)

# Optionally register other models directly if you want to manage them separately
admin.site.register(FamilyMember)
admin.site.register(EducationalQualification)
admin.site.register(EmploymentRecord)
admin.site.register(LanguageProficiency)
admin.site.register(Reference)



