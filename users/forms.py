from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import Profile, FamilyMember, EmploymentRecord, EducationalQualification, LanguageProficiency, Reference

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Profile.user.field.related_model
        fields = ('username', 'password')

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Profile.user.field.related_model
        fields = ('username', 'email', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Profile.user.field.related_model
        fields = ('username', 'email',)

class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'employee_code', 
            'first_name',
            'middle_name',
            'last_name', 
            'designation',
            'email',
            'phone_number',
            'date_of_joining',
            'picture',
            'father_name',
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
        fields = ['bank_name', 'ifsc_code', 'bank_account_number']

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

FamilyMemberFormSet = forms.modelformset_factory(
    FamilyMember,
    form=FamilyDetailsForm,
    extra=3
)

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

class EmploymentRecordForm(forms.ModelForm):
    class Meta:
        model = EmploymentRecord
        fields = ['organization', 'designation', 'joining_date', 'leaving_date', 'document']
        widgets = {
            'joining_date': forms.DateInput(attrs={'type': 'date'}),
            'leaving_date': forms.DateInput(attrs={'type': 'date'}),
            'organization': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'document': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ReferencesForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = ['name', 'occupation', 'phone_number', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class LanguageProficiencyForm(forms.ModelForm):
    class Meta:
        model = LanguageProficiency
        fields = ['language', 'speak', 'read', 'write']
        widgets = {
            'language': forms.TextInput(attrs={'class': 'form-control'}),
            'speak': forms.Select(attrs={'class': 'form-control'}),
            'read': forms.Select(attrs={'class': 'form-control'}),
            'write': forms.Select(attrs={'class': 'form-control'}),
        }

LanguageProficiencyFormSet = forms.modelformset_factory(
    LanguageProficiency,
    form=LanguageProficiencyForm,
    extra=1
)
