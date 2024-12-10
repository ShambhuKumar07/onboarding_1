from django.contrib import admin
from .models import (
    CustomUser, Profile, FamilyMember, EducationalQualification, EmploymentRecord, 
    LanguageProficiency, Reference
)
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from compliance.models import Employee  # Import the Employee model
from compliance.admin import EmployeeInline
from compensation.models import EmployeeCTC
from import_export.admin import ImportExportModelAdmin, ExportMixin
from import_export import resources
from import_export.widgets import ForeignKeyWidget


# Register the inlines
class FamilyMemberInline(admin.TabularInline):
    model = FamilyMember
    extra = 1  # Number of extra forms to show

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
    model = EmployeeCTC
    extra = 1


# Resources for import/export
# class ProfileResource(resources.ModelResource):
#     class Meta:
#         model = Profile
#         fields = ('user__username', 'first_name', 'middle_name', 'last_name', 'Employee_Code', 'designation')

from import_export import resources, fields
from import_export.widgets import ManyToManyWidget


'''class ProfileResource(resources.ModelResource):
    # Profile Fields
    user = fields.Field(attribute='user__username', column_name='Username')
    first_name = fields.Field(attribute='first_name', column_name='First Name')
    middle_name = fields.Field(attribute='middle_name', column_name='Middle Name')
    last_name = fields.Field(attribute='last_name', column_name='Last Name')
    Employee_Code = fields.Field(attribute='Employee_Code', column_name='Employee Code')
    designation = fields.Field(attribute='designation', column_name='Designation')
    email = fields.Field(attribute='email', column_name='Email')
    date_of_joining = fields.Field(attribute='date_of_joining', column_name='Date of Joining')

    # FamilyMember Fields
    family_relation = fields.Field(column_name='Family Relation', attribute='family_members__relation')
    family_member_name = fields.Field(column_name='Family Member Name', attribute='family_members__name')
    family_member_dob = fields.Field(column_name='Family Member Date of Birth', attribute='family_members__date_of_birth')
    family_member_sex = fields.Field(column_name='Family Member Sex', attribute='family_members__sex')
    family_member_age = fields.Field(column_name='Family Member Age', attribute='family_members__age')

    # EducationalQualification Fields
    qualification = fields.Field(column_name='Examination Passed', attribute='educational_qualifications__examination_passed')
    year_of_passing = fields.Field(column_name='Year of Passing', attribute='educational_qualifications__year_of_passing')
    school_or_college = fields.Field(column_name='School/College', attribute='educational_qualifications__school_or_college')
    subjects = fields.Field(column_name='Subjects', attribute='educational_qualifications__subjects')
    division = fields.Field(column_name='Division', attribute='educational_qualifications__division')

    # EmploymentRecord Fields
    organization = fields.Field(column_name='Organization', attribute='employment_records__organization')
    designation = fields.Field(column_name='Employment Designation', attribute='employment_records__designation')
    joining_date = fields.Field(column_name='Joining Date', attribute='employment_records__joining_date')
    leaving_date = fields.Field(column_name='Leaving Date', attribute='employment_records__leaving_date')

    # LanguageProficiency Fields
    language = fields.Field(column_name='Language', attribute='languages__language')
    speak = fields.Field(column_name='Speak Proficiency', attribute='languages__speak')
    read = fields.Field(column_name='Read Proficiency', attribute='languages__read')
    write = fields.Field(column_name='Write Proficiency', attribute='languages__write')

    # Reference Fields
    reference_name = fields.Field(column_name='Reference Name', attribute='references__name')
    reference_occupation = fields.Field(column_name='Reference Occupation', attribute='references__occupation')
    reference_phone = fields.Field(column_name='Reference Phone Number', attribute='references__phone_number')
    reference_email = fields.Field(column_name='Reference Email', attribute='references__email')

    class Meta:
        model = Profile
        fields = (
            'user', 'first_name', 'middle_name', 'last_name', 'Employee_Code', 'designation', 'email', 'date_of_joining',
            'family_relation', 'family_member_name', 'family_member_dob', 'family_member_sex', 'family_member_age',
            'qualification', 'year_of_passing', 'school_or_college', 'subjects', 'division',
            'organization', 'designation', 'joining_date', 'leaving_date',
            'language', 'speak', 'read', 'write',
            'reference_name', 'reference_occupation', 'reference_phone', 'reference_email'
        )
        export_order = fields  # Optional: This ensures the fields are exported in the specified order


'''
# class ProfileResource(resources.ModelResource):
#     # Profile Fields
#     user = fields.Field(attribute='user__username', column_name='Username')
#     first_name = fields.Field(attribute='first_name', column_name='First Name')
#     middle_name = fields.Field(attribute='middle_name', column_name='Middle Name')
#     last_name = fields.Field(attribute='last_name', column_name='Last Name')
#     Employee_Code = fields.Field(attribute='Employee_Code', column_name='Employee Code')
#     designation = fields.Field(attribute='designation', column_name='Designation')
#     email = fields.Field(attribute='email', column_name='Email')
#     date_of_joining = fields.Field(attribute='date_of_joining', column_name='Date of Joining')

#     # Custom methods to handle many-to-one relationships for export
#     family_members = fields.Field(column_name='Family Members', attribute='family_members', readonly=True)
#     educational_qualifications = fields.Field(column_name='Educational Qualifications', attribute='educational_qualifications', readonly=True)
#     employment_records = fields.Field(column_name='Employment Records', attribute='employment_records', readonly=True)
#     language_proficiencies = fields.Field(column_name='Languages Known', attribute='languages', readonly=True)
#     references = fields.Field(column_name='References', attribute='references', readonly=True)

#     def dehydrate_family_members(self, profile):
#         return ', '.join([f'{fm.relation}: {fm.name} (DOB: {fm.date_of_birth})' for fm in profile.family_members.all()])

#     def dehydrate_educational_qualifications(self, profile):
#         return ', '.join([f'{eq.examination_passed} ({eq.year_of_passing}) - {eq.school_or_college}' for eq in profile.educational_qualifications.all()])

#     def dehydrate_employment_records(self, profile):
#         return ', '.join([f'{er.organization}: {er.designation} (Joined: {er.joining_date}, Left: {er.leaving_date})' for er in profile.employment_records.all()])

#     def dehydrate_language_proficiencies(self, profile):
#         return ', '.join([f'{lp.language} (Speak: {lp.speak}, Read: {lp.read}, Write: {lp.write})' for lp in profile.languages.all()])

#     def dehydrate_references(self, profile):
#         return ', '.join([f'{ref.name}: {ref.occupation} (Phone: {ref.phone_number}, Email: {ref.email})' for ref in profile.references.all()])

#     class Meta:
#         model = Profile
#         fields = (
#             'user', 'first_name', 'middle_name', 'last_name', 'Employee_Code', 'designation', 'email', 'date_of_joining',
#             'family_members', 'educational_qualifications', 'employment_records', 'language_proficiencies', 'references'
#         )
#         export_order = fields  # Optional: This ensures the fields are exported in the specified order

from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget


from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Profile, FamilyMember, EducationalQualification, EmploymentRecord, LanguageProficiency, Reference

class ProfileResource(resources.ModelResource):
    # Profile Fields
    user = fields.Field(attribute='user__username', column_name='Username')
    first_name = fields.Field(attribute='first_name', column_name='First Name')
    middle_name = fields.Field(attribute='middle_name', column_name='Middle Name')
    last_name = fields.Field(attribute='last_name', column_name='Last Name')
    employee_code = fields.Field(attribute='employee_code', column_name='Employee Code')
    designation = fields.Field(attribute='designation', column_name='Designation')
    email = fields.Field(attribute='email', column_name='Email')
    date_of_joining = fields.Field(attribute='date_of_joining', column_name='Date of Joining')

    # FamilyMember Fields (assuming one-to-many relationship)
    family_member_relation_1 = fields.Field(column_name='Family Member 1 Relation', attribute='family_members__relation')
    family_member_name_1 = fields.Field(column_name='Family Member 1 Name', attribute='family_members__name')
    family_member_dob_1 = fields.Field(column_name='Family Member 1 Date of Birth', attribute='family_members__date_of_birth')

    # EducationalQualification Fields (assuming one-to-many relationship)
    qualification_1 = fields.Field(column_name='Qualification 1', attribute='educational_qualifications__examination_passed')
    year_of_passing_1 = fields.Field(column_name='Year of Passing 1', attribute='educational_qualifications__year_of_passing')
    school_or_college_1 = fields.Field(column_name='School/College 1', attribute='educational_qualifications__school_or_college')

    # EmploymentRecord Fields (assuming one-to-many relationship)
    organization_1 = fields.Field(column_name='Organization 1', attribute='employment_records__organization')
    employment_designation_1 = fields.Field(column_name='Designation 1', attribute='employment_records__designation')

    # LanguageProficiency Fields (assuming one-to-many relationship)
    language_1 = fields.Field(column_name='Language 1', attribute='languages__language')
    speak_proficiency_1 = fields.Field(column_name='Speak Proficiency 1', attribute='languages__speak')

    # Reference Fields (assuming one-to-many relationship)
    reference_name_1 = fields.Field(column_name='Reference 1 Name', attribute='references__name')
    reference_occupation_1 = fields.Field(column_name='Reference 1 Occupation', attribute='references__occupation')

    class Meta:
        model = Profile
        fields = (
            'user', 'first_name', 'middle_name', 'last_name', 'employee_code', 'designation', 'email', 'date_of_joining',
            'family_member_relation_1', 'family_member_name_1', 'family_member_dob_1',
            'qualification_1', 'year_of_passing_1', 'school_or_college_1',
            'organization_1', 'employment_designation_1',
            'language_1', 'speak_proficiency_1',
            'reference_name_1', 'reference_occupation_1'
        )

    def get_queryset(self):
        # Use prefetch_related to optimize the related queries
        return Profile.objects.prefetch_related(
            'family_members', 'educational_qualifications', 
            'employment_records', 'languages', 'references'
        )



class FamilyMemberResource(resources.ModelResource):
    class Meta:
        model = FamilyMember
        fields = ('profile__user__username', 'relation', 'name', 'date_of_birth', 'sex', 'age')

class EducationalQualificationResource(resources.ModelResource):
    class Meta:
        model = EducationalQualification
        fields = ('profile__user__username', 'examination_passed', 'year_of_passing', 'school_or_college', 'subjects', 'division', 'document')

class EmploymentRecordResource(resources.ModelResource):
    class Meta:
        model = EmploymentRecord
        fields = ('profile__user__username', 'organization', 'designation', 'joining_date', 'leaving_date', 'document')

class LanguageProficiencyResource(resources.ModelResource):
    class Meta:
        model = LanguageProficiency
        fields = ('profile__user__username', 'language', 'speak', 'read', 'write')

class ReferenceResource(resources.ModelResource):
    class Meta:
        model = Reference
        fields = ('profile__user__username', 'name', 'occupation', 'phone_number', 'email')


# Admin for Profile
class ProfileAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ProfileResource
    inlines = [
        FamilyMemberInline, EducationalQualificationInline, EmploymentRecordInline,
        LanguageProficiencyInline, ReferenceInline, EmployeeInline, EmployeeCTCInline
    ]
    # list_display = ('id','user', 'Employee_Code', 'first_name', 'last_name')
    list_display = ('user', 'employee_code', 'first_name', 'last_name')

    search_fields = ('user__username', 'first_name', 'last_name', 'employee_code')


# Admin for FamilyMember
class FamilyMemberAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = FamilyMemberResource

# Admin for EducationalQualification
class EducationalQualificationAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = EducationalQualificationResource

# Admin for EmploymentRecord
class EmploymentRecordAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = EmploymentRecordResource

# Admin for LanguageProficiency
class LanguageProficiencyAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = LanguageProficiencyResource

# Admin for Reference
class ReferenceAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ReferenceResource


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


# Register the resources with the admin site
admin.site.register(FamilyMember, FamilyMemberAdmin)
admin.site.register(EducationalQualification, EducationalQualificationAdmin)
admin.site.register(EmploymentRecord, EmploymentRecordAdmin)
admin.site.register(LanguageProficiency, LanguageProficiencyAdmin)
admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
