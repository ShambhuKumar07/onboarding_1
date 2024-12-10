# applicant/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PersonalInformationForm
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
from .forms import BankDetailsForm
 

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
            # Save form data to the database or process it as needed
            # Example: Save data to a model
            # form.save()
            return redirect('applicant:dashboard')
    else:
        form = PersonalInformationForm()
    return render(request, 'applicant/page_1.html', {'form': form})


def save_page_1(request):
    if request.method == 'POST':
        form = PersonalInformationForm(request.POST)
        if form.is_valid():
            # Create or update Applicant instance based on the form data
            # Here we assume you have a way to associate the Applicant with the logged-in user
            applicant = Applicant.objects.get(user=request.user)  # Adjust this as needed

            applicant.employee_code = form.cleaned_data['employee_code']
            applicant.designation = form.cleaned_data['designation']
            applicant.date_of_joining = form.cleaned_data['date_of_joining']
            applicant.first_name = form.cleaned_data['first_name']
            applicant.middle_name = form.cleaned_data['middle_name']
            applicant.surname = form.cleaned_data['surname']
            applicant.husband_father_name = form.cleaned_data['husband_father_name']
            applicant.mother_name = form.cleaned_data['mother_name']
            applicant.date_of_birth = form.cleaned_data['date_of_birth']
            applicant.gender = form.cleaned_data['gender']
            applicant.blood_group = form.cleaned_data['blood_group']
            applicant.present_address = form.cleaned_data['present_address']
            applicant.permanent_address = form.cleaned_data['permanent_address']
            applicant.pan_no = form.cleaned_data['pan_no']
            applicant.marital_status = form.cleaned_data['marital_status']
            applicant.date_of_marriage = form.cleaned_data['date_of_marriage']

            applicant.save()  # Save the instance to the database

            return redirect('applicant:dashboard')
    else:
        form = PersonalInformationForm()
    return render(request, 'applicant/page_1.html', {'form': form})



def page_2(request):
    # print("Page 2 view accessed")  # Debug statement
    
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect('applicant:dashboard')

    if request.method == 'POST':
        form = BankDetailsForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('applicant:dashboard')
    else:
        form = BankDetailsForm(instance=profile)

    return render(request, 'applicant/page_2.html', {'form': form})



def page_3(request):
    try:
        profile = Profile.objects.get(user=request.user)  # Get the Profile linked to the logged-in user
    except Profile.DoesNotExist:
        return redirect('applicant:dashboard')  # Redirect if no profile exists

    if request.method == 'POST':
        form = EmergencyContactForm(request.POST, instance=profile)  # Pass the profile instance to the form
        if form.is_valid():
            form.save()  # Save the emergency contact details to the Profile model
            return redirect('applicant:dashboard')
    else:
        form = EmergencyContactForm(instance=profile)  # Prepopulate the form with current profile data

    return render(request, 'applicant/page_3.html', {'form': form})


# def page_4(request):
#     return render(request, 'applicant/page_4.html')


def page_4(request):
    try:
        profile = Profile.objects.get(user=request.user)  # Get the Profile linked to the logged-in user
    except Profile.DoesNotExist:
        return redirect('applicant:dashboard')  # Redirect if no profile exists

    if request.method == 'POST':
        form = FamilyDetailsForm(request.POST, instance=profile)
        if form.is_valid():
            # Save the form data to the profile or handle the family data accordingly
            form.save()
            return redirect('applicant:dashboard')
    else:
        form = FamilyDetailsForm(instance=profile)  # Prepopulate with existing data

    return render(request, 'applicant/page_4.html', {'form': form})



def page_5(request):
    if request.method == 'POST':
        form = EducationalQualificationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('applicant:dashboard')  # Redirect after saving
        else:
            print("Form errors:", form.errors)
    else:
        form = EducationalQualificationForm()

    return render(request, 'applicant/page_5.html', {'form': form})


# def page_6(request):
#     return render(request, 'applicant/page_6.html')

def page_6(request):
    try:
        profile = Profile.objects.get(user=request.user)  # Ensure the user has a profile
    except Profile.DoesNotExist:
        return redirect('applicant:dashboard')  # Redirect to the dashboard if no profile exists

    if request.method == 'POST':
        form = EmploymentRecordForm(request.POST)
        if form.is_valid():
            employment_record = form.save(commit=False)
            employment_record.profile = profile  # Link the employment record to the user's profile
            employment_record.save()
            return redirect('applicant:dashboard')
    else:
        form = EmploymentRecordForm()

    return render(request, 'applicant/page_6.html', {'form': form})



# def page_7(request):
#     return render(request, 'applicant/page_7.html')



def page_7(request):
    if request.method == 'POST':
        form = ReferencesForm(request.POST)
        if form.is_valid():
            # Process the form data as needed
            name_1 = form.cleaned_data['name_1']
            occupation_1 = form.cleaned_data['occupation_1']
            tel_no_1 = form.cleaned_data['tel_no_1']
            email_1 = form.cleaned_data['email_1']

            name_2 = form.cleaned_data['name_2']
            occupation_2 = form.cleaned_data['occupation_2']
            tel_no_2 = form.cleaned_data['tel_no_2']
            email_2 = form.cleaned_data['email_2']


            return redirect('applicant:dashboard')  # Redirect after submission
    else:
        form = ReferencesForm()

    return render(request, 'applicant/page_7.html', {'form': form})




# applicant/views.py

from django.shortcuts import render, redirect
from .forms import LanguageProficiencyForm
from .models import LanguageProficiency

def languages_known(request):
    if request.method == 'POST':
        form = LanguageProficiencyForm(request.POST)
        if form.is_valid():
            language_proficiency = form.save(commit=False)
            language_proficiency.user = request.user
            language_proficiency.save()
            return redirect('applicant:dashboard')
    else:
        form = LanguageProficiencyForm()
    return render(request, 'applicant/languages_known.html', {'form': form})
