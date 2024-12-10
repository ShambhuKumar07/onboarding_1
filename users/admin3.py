from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Profile, FamilyMember, EducationalQualification, EmploymentRecord, LanguageProficiency, Reference

class ProfileResource(resources.ModelResource):
    # Adding fields for related data
    family_members = fields.Field(column_name='family_members')
    educational_qualifications = fields.Field(column_name='educational_qualifications')
    employment_records = fields.Field(column_name='employment_records')
    language_proficiencies = fields.Field(column_name='language_proficiencies')
    references = fields.Field(column_name='references')

    class Meta:
        model = Profile
        fields = ('user__username', 'Employee_Code', 'first_name', 'last_name')  # Fields to include from Profile

    # Overriding dehydrate methods to pull related data
    def dehydrate_family_members(self, profile):
        # Concatenating all family members into a single string
        return ', '.join([f'{fm.name} ({fm.relation})' for fm in profile.familymember_set.all()])

    def dehydrate_educational_qualifications(self, profile):
        # Concatenating educational qualifications
        return ', '.join([f'{eq.degree} from {eq.institution}' for eq in profile.educationalqualification_set.all()])

    def dehydrate_employment_records(self, profile):
        # Concatenating employment records
        return ', '.join([f'{er.company_name} - {er.position}' for er in profile.employmentrecord_set.all()])

    def dehydrate_language_proficiencies(self, profile):
        # Concatenating language proficiencies
        return ', '.join([f'{lp.language} (Speaking: {lp.speaking_proficiency}, Reading: {lp.reading_proficiency}, Writing: {lp.writing_proficiency})' 
                          for lp in profile.languageproficiency_set.all()])

    def dehydrate_references(self, profile):
        # Concatenating references
        return ', '.join([f'{ref.name} ({ref.relation})' for ref in profile.reference_set.all()])



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



from import_export.admin import ImportExportModelAdmin
# from .resources import ProfileResource  # Import the resource

class ProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProfileResource  # Register the resource class
    inlines = [
        FamilyMemberInline, 
        EducationalQualificationInline, 
        EmploymentRecordInline, 
        LanguageProficiencyInline, 
        ReferenceInline, 
        EmployeeInline, 
        EmployeeCTCInline
    ]
    list_display = ('user', 'Employee_Code', 'first_name', 'last_name')
    search_fields = ('user__username', 'first_name', 'last_name', 'Employee_Code')

# Register the admin
admin.site.register(Profile, ProfileAdmin)
