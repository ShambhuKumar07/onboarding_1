from django.db import models
from applicant.models import Applicant
from users.models import Profile  # Import the Profile model
# Create your models here.
class EmployeeSalary(models.Model):
    basic = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Basic Salary")
    hra = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="HRA")
    special_allowance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Special Allowance")

    def gross_salary(self):
        return self.basic + self.hra + self.special_allowance

    def __str__(self):
        return f"Basic: {self.basic}, HRA: {self.hra}, Special Allowance: {self.special_allowance}"
    
class employee_deduction(models.Model):

    pf_deduction=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="PF_Deduction")
    asic_deduction=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="ASIC_Deduction")
    def emp_deduction(self):
        return self.pf_deduction + self.asic_deduction

    def __str__(self):
        return f"PF_Deduction:{self.pf_deduction}, ASIC_Deduction:{self.asic_deduction}"

class EmployeeContribution(models.Model):
    pf_emp_contribution = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="PF (Employers Contribution)")
    esic_emp_contribution = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="ESIC (Employers Contribution)")
    mediclaim = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Mediclaim")
    gratuity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Gratuity")

    # Calculate total employee contribution
    def emp_contribution(self):
        return self.pf_emp_contribution + self.esic_emp_contribution + self.mediclaim + self.gratuity

    def __str__(self): 
        return f"Gratuity: {self.gratuity}, Total Contribution: {self.emp_contribution()}"

class EmployeeCTC(models.Model):
    # applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    
    applicant = models.ForeignKey(Applicant, null=True, blank=True, on_delete=models.CASCADE)  # Allow null
    profile = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)  # Add ForeignKey to Profile
    salary = models.OneToOneField(EmployeeSalary, on_delete=models.CASCADE)  # Correct the model reference
    contribution = models.OneToOneField(EmployeeContribution, on_delete=models.CASCADE)  # Correct the model reference
    deduction = models.OneToOneField(employee_deduction, on_delete=models.CASCADE)  # Correct the model reference
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    # created_at = models.DateTimeField(default='2023-01-01 00:00:00')  # Temporary default value
    
    def calculate_ctc(self):
        # Calculate CTC: Gross Salary + Employer's Contribution - Employee's Deductions
        return self.salary.gross_salary() + self.contribution.emp_contribution() - self.deduction.emp_deduction()
