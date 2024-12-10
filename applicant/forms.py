from django import forms

from users.models import Profile,EducationalQualification  # Import the Profile model 
# from .models import EducationalQualification

# applicant/forms.py

from django import forms
from users.models import Profile, FamilyMember  # Import the Profile model

class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'employee_code',  # Employee Code
            'first_name',
            'middle_name',
            'last_name',  # Surname
            'designation',
            'email',
            'phone_number',
            'date_of_joining',
            'picture',
            
            'father_name',  # Husband/Father's Name
            'mother_name',
            'date_of_birth',
            'gender',
            'blood_group',
            'present_address',
            'permanent_address',
            'pan_number',
            'marital_status',
        ]

    date_of_marriage = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)


class BankDetailsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bank_name', 'ifsc_code', 'bank_account_number']  # Bank-related fields from Profile

class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['emergency_contact_name', 'emergency_contact_relation', 'emergency_contact_number']

class FamilyDetailsForm(forms.ModelForm):
    class Meta:
        model = FamilyMember
        fields = ['relation', 'name', 'date_of_birth', 'sex', 'age']

    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    sex = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])

from django.forms import modelformset_factory
 
FamilyMemberFormSet = modelformset_factory(
    FamilyMember,
    form=FamilyDetailsForm,
    extra=3  # Adjust the number of extra forms as needed
)



# applicant/models's filed
# class EducationalQualificationForm(forms.ModelForm):
#     class Meta:
#         model = EducationalQualification
#         fields = ['exam_passed', 'year_of_passing', 'school_college_university', 'subjects', 'division', 'document']
#         widgets = {
#             'exam_passed': forms.TextInput(attrs={'class': 'form-control'}),
#             'year_of_passing': forms.NumberInput(attrs={'class': 'form-control'}),
#             'school_college_university': forms.TextInput(attrs={'class': 'form-control'}),
#             'subjects': forms.TextInput(attrs={'class': 'form-control'}),
#             'division': forms.TextInput(attrs={'class': 'form-control'}),
#             'document': forms.ClearableFileInput(attrs={'class': 'form-control'}),  # New field
#         }




class EducationalQualificationForm(forms.ModelForm):
    class Meta:
        model = EducationalQualification
        fields = ['examination_passed', 'year_of_passing', 'school_or_college', 'subjects', 'division', 'document']
        widgets = {
            'examination_passed': forms.TextInput(attrs={'class': 'form-control'}),
            'year_of_passing': forms.NumberInput(attrs={'class': 'form-control'}),
            'school_or_college': forms.TextInput(attrs={'class': 'form-control'}),
            'subjects': forms.TextInput(attrs={'class': 'form-control'}),
            'division': forms.TextInput(attrs={'class': 'form-control'}),
            'document': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }





from django import forms
from users.models import EmploymentRecord

class EmploymentRecordForm(forms.ModelForm):
    joining_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    leaving_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    organization = forms.CharField(max_length=255)
    designation = forms.CharField(max_length=100)
    document = forms.FileField(required=False)  # New field for document upload

    class Meta:
        model = EmploymentRecord
        fields = ['organization', 'designation', 'joining_date', 'leaving_date', 'document']  # Include document in fields

from django import forms

# class ReferencesForm(forms.Form):
#     name_1 = forms.CharField(max_length=100, label="Name (Reference 1)")
#     occupation_1 = forms.CharField(max_length=100, label="Occupation (Reference 1)")
#     tel_no_1 = forms.CharField(max_length=15, label="Tel. No. (Reference 1)")
#     email_1 = forms.EmailField(label="Email (Reference 1)")

#     name_2 = forms.CharField(max_length=100, label="Name (Reference 2)")
#     occupation_2 = forms.CharField(max_length=100, label="Occupation (Reference 2)")
#     tel_no_2 = forms.CharField(max_length=15, label="Tel. No. (Reference 2)")
#     email_2 = forms.EmailField(label="Email (Reference 2)")



from django import forms
from users.models import Reference

class ReferencesForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = ['name', 'occupation', 'phone_number', 'email']
        labels = {
            'name': 'Name (Reference)',
            'occupation': 'Occupation (Reference)',
            'phone_number': 'Tel. No. (Reference)',
            'email': 'Email (Reference)',
        }

# applicant/forms.py

from django import forms
from users.models import LanguageProficiency

class LanguageProficiencyForm(forms.ModelForm):
    class Meta:
        model = LanguageProficiency
        fields = ['language', 'speak', 'read', 'write']
        widgets = {
            'speak': forms.RadioSelect(choices=[('A', 'Fluent'), ('B', 'Fair'), ('C', 'Workable')]),
            'read': forms.RadioSelect(choices=[('A', 'Fluent'), ('B', 'Fair'), ('C', 'Workable')]),
            'write': forms.RadioSelect(choices=[('A', 'Fluent'), ('B', 'Fair'), ('C', 'Workable')]),
        }
