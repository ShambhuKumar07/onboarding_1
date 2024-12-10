# applicant/views.py
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PersonalInformationForm
from .models import Applicant
from .forms import BankDetailsForm
from users.models import Profile   
from .forms import EmergencyContactForm
from .forms import FamilyDetailsForm
from .forms import EmploymentRecordForm
from users.models import EmploymentRecord, Profile
from .forms import ReferencesForm
from .forms import EducationalQualificationForm
from .forms import LanguageProficiencyForm
from .models import LanguageProficiency
from users.models import Profile, LanguageProficiency  # Ensure you import the models 
from users.models import Profile, Reference,FamilyMember
from users.models import EducationalQualification

@login_required
def applicant_dashboard(request):
    # Fetch applicant-specific information if needed
    context = {
        'applicant': request.user.applicant  # assuming each user has an applicant profile
    }
    return render(request, 'applicant/dashboard.html', context)

def page_1(request):
    if request.method == 'POST':
        form = PersonalInformationForm(request.POST)
        if form.is_valid():
            profile, created = Profile.objects.get_or_create(user=request.user)
            for field, value in form.cleaned_data.items():
                setattr(profile, field, value)
            profile.save()

            # Link the profile to the applicant if not already linked
            applicant, created = Applicant.objects.get_or_create(user=request.user)
            applicant.profile = profile
            applicant.save()

            return redirect('applicant:page_2')
        else:
            print("Form is not valid:", form.errors)
    else:
        form = PersonalInformationForm()
    return render(request, 'applicant/page_1.html', {'form': form})

 
def page_2(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect('applicant:dashboard')

    if request.method == 'POST':
        form = BankDetailsForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('applicant:page_3')  # Redirect to page 3
    else:
        form = BankDetailsForm(instance=profile)

    return render(request, 'applicant/page_2.html', {'form': form})
 
def page_3(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect('applicant:dashboard')

    if request.method == 'POST':
        form = EmergencyContactForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('applicant:page_4')  # Redirect to page 4
    else:
        form = EmergencyContactForm(instance=profile)

    return render(request, 'applicant/page_3.html', {'form': form})

def page_4(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect('applicant:dashboard')

    if request.method == 'POST':
        form = FamilyDetailsForm(request.POST)
        if form.is_valid():
            # Create a new FamilyMember instance, associating it with the Profile
            family_member = form.save(commit=False)
            family_member.profile = profile
            family_member.save()
            return redirect('applicant:page_5')  # Redirect to page 5
    else:
        form = FamilyDetailsForm()

    return render(request, 'applicant/page_4.html', {'form': form})

def page_5(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect('applicant:dashboard')

    if request.method == 'POST':
        qualifications = []
        for i in range(len(request.POST.getlist('examination_passed'))):
            form = EducationalQualificationForm({
                'examination_passed': request.POST.getlist('examination_passed')[i],
                'year_of_passing': request.POST.getlist('year_of_passing')[i],
                'school_or_college': request.POST.getlist('school_or_college')[i],
                'subjects': request.POST.getlist('subjects')[i],
                'division': request.POST.getlist('division')[i],
            }, {
                'document': request.FILES.getlist('document')[i] if len(request.FILES.getlist('document')) > i else None,
            })
            
            if form.is_valid():
                qualification = form.save(commit=False)
                qualification.profile = profile
                qualifications.append(qualification)
            else:
                print("Form errors:", form.errors)
                
        EducationalQualification.objects.bulk_create(qualifications)
        return redirect('applicant:page_6')  # Redirect to page 6
    else:
        form = EducationalQualificationForm()

    return render(request, 'applicant/page_5.html', {'form': form})
 
def page_6(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect('applicant:dashboard')

    if request.method == 'POST':
        form = EmploymentRecordForm(request.POST)
        if form.is_valid():
            employment_record = form.save(commit=False)
            employment_record.profile = profile
            employment_record.save()
            return redirect('applicant:languages_known')  # Redirect to languages known page
    else:
        form = EmploymentRecordForm()

    return render(request, 'applicant/page_6.html', {'form': form})

def languages_known(request):
    try:
        profile = Profile.objects.get(user=request.user)  # Fetch the profile linked to the current user
    except Profile.DoesNotExist:
        return redirect('applicant:dashboard')  # Redirect if no profile exists

    if request.method == 'POST':
        form = LanguageProficiencyForm(request.POST)
        if form.is_valid():
            language_proficiency = form.save(commit=False)
            language_proficiency.profile = profile  # Assign the profile correctly
            language_proficiency.save()
            return redirect('applicant:page_7')  # Redirect to page 7
    else:
        form = LanguageProficiencyForm()
    
    return render(request, 'applicant/languages_known.html', {'form': form})

def page_7(request):
    try:
        profile = Profile.objects.get(user=request.user)  # Fetch the profile linked to the current user
    except Profile.DoesNotExist:
        return redirect('applicant:dashboard')  # Redirect if no profile exists

    if request.method == 'POST':
        form1 = ReferencesForm(request.POST, prefix='ref1')
        form2 = ReferencesForm(request.POST, prefix='ref2')

        if form1.is_valid() and form2.is_valid():
            # Save the first reference
            ref1 = form1.save(commit=False)
            ref1.profile = profile
            ref1.save()

            # Save the second reference
            ref2 = form2.save(commit=False)
            ref2.profile = profile
            ref2.save()

            return redirect('applicant:dashboard')  # Redirect to the dashboard after the last page
    else:
        form1 = ReferencesForm(prefix='ref1')
        form2 = ReferencesForm(prefix='ref2')

    return render(request, 'applicant/page_7.html', {'form1': form1, 'form2': form2})
