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


from import_export import resources,fields
from import_export.widgets import ManyToManyWidget

class ProfileResource(resources.ModelResource):
    family_members = fields.Field(attribute='familymember_set', widget=ManyToManyWidget(FamilyMember, separator=',', field='name'), column_name='Family Members')
    educational_qualifications = fields.Field(attribute='educationalqualification_set', widget=ManyToManyWidget(EducationalQualification, separator=',', field='degree'), column_name='Educational Qualifications')

    class Meta:
        model = Profile
        fields = (
            'user__username', 
            'Employee_Code', 
            'first_name', 
            'last_name', 
            'phone_number', 
            'address', 
            'family_members',  # Add related fields
            'educational_qualifications'  # Add related fields
        )
        export_order = (
            'user__username', 
            'Employee_Code', 
            'first_name', 
            'last_name', 
            'phone_number', 
            'address', 
            'family_members', 
            'educational_qualifications'
        )

from django.http import HttpResponse
import csv


def export_specific_profiles(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="specific_profiles.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['User', 'Employee Code', 'First Name', 'Last Name', 'Phone Number', 'Family Members', 'Educational Qualifications'])
    
    for profile in queryset.filter(Employee_Code__startswith="EMP"):  # Example condition to filter profiles
        family_members = ', '.join([fm.name for fm in profile.familymember_set.all()])
        educational_qualifications = ', '.join([eq.degree for eq in profile.educationalqualification_set.all()])
        writer.writerow([
            profile.user.username, 
            profile.Employee_Code, 
            profile.first_name, 
            profile.last_name, 
            profile.phone_number, 
            family_members, 
            educational_qualifications
        ])
    
    return response


# Admin for Profile
class ProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    resource_class = ProfileResource

    inlines = [FamilyMemberInline, EducationalQualificationInline, EmploymentRecordInline, LanguageProficiencyInline, ReferenceInline,EmployeeInline,EmployeeCTCInline]
    list_display = ('user', 'Employee_Code', 'first_name', 'last_name')
    search_fields = ('user__username', 'first_name', 'last_name', 'Employee_Code')
    actions = [export_specific_profiles] 

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
