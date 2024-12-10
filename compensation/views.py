
from django.shortcuts import render, redirect
from .forms import EmployeeSalaryForm, EmployeeContributionForm, EmployeeDeductionForm
from .models import EmployeeCTC,employee_deduction
from django.contrib.auth.decorators import login_required
from applicant.models import Applicant  # Import the Applicant model

# @login_required
# def employee_ctc_view(request):
#     gross_salary = None
#     total_contribution = None
#     total_deduction = None
#     ctc_value = None

#     if request.method == 'POST':
#         salary_form = EmployeeSalaryForm(request.POST)
#         contribution_form = EmployeeContributionForm(request.POST)
#         deduction_form = EmployeeDeductionForm(request.POST)

#         if salary_form.is_valid() and contribution_form.is_valid() and deduction_form.is_valid():
#             salary = salary_form.save()
#             contribution = contribution_form.save()
#             deduction = deduction_form.save()

#             # Calculate gross salary
#             gross_salary = salary.gross_salary()

#             # Get the applicant for the logged-in user
#             applicant = request.user.applicant  # Assuming each user has an Applicant profile

#             # Create and save EmployeeCTC including deduction and associate with the applicant
#             ctc = EmployeeCTC.objects.create(
#                 salary=salary,
#                 contribution=contribution,
#                 deduction=deduction,
#                 applicant=applicant  # Associate with the applicant
#             )

#             # Calculate CTC (Gross Salary + Employer's Contribution - Deductions)
#             ctc_value = ctc.calculate_ctc()

#             return redirect('success_page')  # Adjust the URL name as per your project

#     else:
#         salary_form = EmployeeSalaryForm()
#         contribution_form = EmployeeContributionForm()
#         deduction_form = EmployeeDeductionForm()

#     return render(request, 'compensation/employee_ctc.html', {
#         'salary_form': salary_form,
#         'contribution_form': contribution_form,
#         'deduction_form': deduction_form,
#         'gross_salary': gross_salary,
#         'total_contribution': total_contribution,
#         'total_deduction': total_deduction,
#         'ctc_value': ctc_value,
#     })


##################### add dropdown of the applicant

@login_required
def employee_ctc_view(request):
    gross_salary = None
    total_contribution = None
    total_deduction = None
    ctc_value = None

    # Retrieve all applicants for the dropdown
    applicants = Applicant.objects.all()

    if request.method == 'POST':
        salary_form = EmployeeSalaryForm(request.POST)
        contribution_form = EmployeeContributionForm(request.POST)
        deduction_form = EmployeeDeductionForm(request.POST)
        selected_applicant_id = request.POST.get('applicant')  # Get selected applicant ID from the form

        if salary_form.is_valid() and contribution_form.is_valid() and deduction_form.is_valid():
            salary = salary_form.save()
            contribution = contribution_form.save()
            deduction = deduction_form.save()

            # Get the selected applicant
            applicant = Applicant.objects.get(id=selected_applicant_id)

            # Create and save EmployeeCTC
            ctc = EmployeeCTC.objects.create(
                salary=salary,
                contribution=contribution,
                deduction=deduction,
                applicant=applicant  # Assign the selected applicant
            )

            # Calculate CTC
            ctc_value = ctc.calculate_ctc()

            return redirect('success_page')

    else:
        salary_form = EmployeeSalaryForm()
        contribution_form = EmployeeContributionForm()
        deduction_form = EmployeeDeductionForm()

    return render(request, 'compensation/employee_ctc.html', {
        'salary_form': salary_form,
        'contribution_form': contribution_form,
        'deduction_form': deduction_form,
        'gross_salary': gross_salary,
        'total_contribution': total_contribution,
        'total_deduction': total_deduction,
        'ctc_value': ctc_value,
        'applicants': applicants,  # Pass the applicants list to the template
    })





# @login_required
# def applicant_compensation_view(request):
#     try:
#         # Fetch compensation details for the logged-in applicant
#         compensation = EmployeeCTC.objects.get(applicant=request.user.applicant)
#     except EmployeeCTC.DoesNotExist:
#         compensation = None  # Handle the case where no compensation data is found

#     return render(request, 'compensation/applicant_compensation.html', {
#         'compensation': compensation,
#     })

################## changes using lates method

@login_required
def applicant_compensation_view(request):
    try:
        # Fetch the latest compensation details for the logged-in applicant
        compensation = EmployeeCTC.objects.filter(applicant=request.user.applicant).latest('created_at')
    except EmployeeCTC.DoesNotExist:
        compensation = None  # Handle the case where no compensation data is found

    return render(request, 'compensation/applicant_compensation.html', {
        'compensation': compensation,
    })



import csv
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import EmployeeCTC, EmployeeSalary, EmployeeContribution, employee_deduction
from applicant.models import Applicant
from django.http import HttpResponse

@login_required
def import_employee_ctc_view(request):
    if request.method == 'POST':
        import_file = request.FILES['import_file']

        # Handle CSV file
        if import_file.name.endswith('.csv'):
            try:
                decoded_file = import_file.read().decode('utf-8').splitlines()
                reader = csv.DictReader(decoded_file)

                for row in reader:
                    # Assuming the CSV file contains these fields
                    applicant_id = row['applicant_id']
                    basic = row['basic']
                    hra = row['hra']
                    special_allowance = row['special_allowance']
                    pf_contribution = row['pf_emp_contribution']
                    esic_contribution = row['esic_emp_contribution']
                    mediclaim = row['mediclaim']
                    gratuity = row['gratuity']
                    pf_deduction = row['pf_deduction']
                    asic_deduction = row['asic_deduction']

                    # Find the applicant
                    applicant = Applicant.objects.get(id=applicant_id)

                    # Create the EmployeeSalary object
                    salary = EmployeeSalary.objects.create(
                        basic=basic,
                        hra=hra,
                        special_allowance=special_allowance
                    )

                    # Create the EmployeeContribution object
                    contribution = EmployeeContribution.objects.create(
                        pf_emp_contribution=pf_contribution,
                        esic_emp_contribution=esic_contribution,
                        mediclaim=mediclaim,
                        gratuity=gratuity
                    )

                    # Create the EmployeeDeduction object
                    deduction = employee_deduction.objects.create(
                        pf_deduction=pf_deduction,
                        asic_deduction=asic_deduction
                    )

                    # Create the EmployeeCTC object
                    EmployeeCTC.objects.create(
                        applicant=applicant,
                        salary=salary,
                        contribution=contribution,
                        deduction=deduction
                    )

                messages.success(request, "CTC data imported successfully.")
            except Exception as e:
                messages.error(request, f"Error occurred during import: {e}")
        else:
            messages.error(request, "Unsupported file format. Please upload a CSV file.")
        
        return redirect('employee_ctc')
    
    return render(request, 'compensation/employee_ctc.html')
