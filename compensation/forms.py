from django import forms
from .models import EmployeeSalary, EmployeeContribution, employee_deduction

class EmployeeSalaryForm(forms.ModelForm):
    gross_salary = forms.DecimalField(required=False, label='Gross Salary', widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = EmployeeSalary
        fields = ['basic', 'hra', 'special_allowance', 'gross_salary']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs and kwargs['instance']:
            # Calculate gross salary if instance is available
            instance = kwargs['instance']
            self.initial['gross_salary'] = instance.gross_salary()

class EmployeeContributionForm(forms.ModelForm):
    class Meta:
        model = EmployeeContribution
        fields = ['pf_emp_contribution', 'esic_emp_contribution', 'mediclaim', 'gratuity']

class EmployeeDeductionForm(forms.ModelForm):
    class Meta:
        model = employee_deduction
        fields = ['pf_deduction', 'asic_deduction']



# from django import forms
# from .models import EmployeeSalary, EmployeeContribution, employee_deduction

# class EmployeeSalaryForm(forms.ModelForm):
#     gross_salary = forms.DecimalField(required=False, label='Gross Salary', widget=forms.TextInput(attrs={'readonly': 'readonly'}))

#     class Meta:
#         model = EmployeeSalary
#         fields = ['basic', 'hra', 'special_allowance', 'gross_salary']

# class EmployeeContributionForm(forms.ModelForm):
#     class Meta:
#         model = EmployeeContribution
#         fields = ['pf_emp_contribution', 'esic_emp_contribution', 'mediclaim', 'gratuity']

# class EmployeeDeductionForm(forms.ModelForm):
#     class Meta:
#         model = employee_deduction
#         fields = ['pf_deduction', 'asic_deduction']
