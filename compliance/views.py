##compliance/views.py

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Employee
# from .models import Compliance  # Import the Compliance model
from django.contrib.auth.decorators import login_required
from applicant.models import Applicant 
 

#################### addd dropdown of the applicant ##################

from django.shortcuts import render, redirect
from .models import Employee
from applicant.models import Applicant

def add_employee(request):
    applicants = Applicant.objects.all()  # Fetch all applicants

    if request.method == 'POST':
        uan_number = request.POST.get('uan_number')
        pan_number = request.POST.get('pan_number')
        esic_number = request.POST.get('esic_number')
        applicant_id = request.POST.get('applicant')  # Get the selected applicant ID

        # Fetch the selected applicant
        applicant = Applicant.objects.get(id=applicant_id)

        # Create and save a new employee record associated with the selected applicant
        Employee.objects.create(
            uan_number=uan_number,
            pan_number=pan_number,
            esic_number=esic_number,
            applicant=applicant
        )
        
        # Redirect to a success page or any other view
        return redirect('employee_success')

    return render(request, 'compliance/employee_form.html', {'applicants': applicants})

def employee_success(request):
    return render(request, 'compliance/employee_success.html')

@login_required
def applicant_compliance_view(request):
    try:
        # Fetch the logged-in applicant
        applicant = request.user.applicant
        employee = Employee.objects.filter(applicant=applicant).first()  # Fetch the first Employee record for this applicant
        
    except Applicant.DoesNotExist:
        employee = None  # Handle case where no applicant is found
    except Employee.DoesNotExist:
        employee = None  # Handle case where no employee record is found

    return render(request, 'compliance/applicant_compliance.html', {
        'employee': employee,
    })
