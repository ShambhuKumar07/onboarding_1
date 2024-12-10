from django.contrib import admin
from .models import EmployeeSalary,employee_deduction,EmployeeContribution,EmployeeCTC

class EmployeeSalaryAdmin(admin.ModelAdmin):
    list_display = ['id','basic', 'hra', 'special_allowance', 'gross_salary_display']

    def gross_salary_display(self, obj):
        return obj.gross_salary()

    gross_salary_display.short_description = 'Gross Salary'

admin.site.register(EmployeeSalary, EmployeeSalaryAdmin)

class EmployeeDeductionAdmin(admin.ModelAdmin):
    list_display = ['pf_deduction', 'asic_deduction', 'total_deduction']

    # Custom method to display total deduction
    def total_deduction(self, obj):
        return obj.emp_deduction()

    total_deduction.short_description = 'Total Deduction'

admin.site.register(employee_deduction, EmployeeDeductionAdmin)

class EmployeeContributionAdmin(admin.ModelAdmin):
    list_display = ['pf_emp_contribution', 'esic_emp_contribution', 'mediclaim', 'gratuity', 'emp_contribution_display']

    def emp_contribution_display(self, obj):
        return obj.emp_contribution()

    emp_contribution_display.short_description = 'Total Contribution'

admin.site.register(EmployeeContribution, EmployeeContributionAdmin)

class EmployeeCTCAdmin(admin.ModelAdmin):
    list_display = ['salary', 'contribution', 'ctc_display']

    def ctc_display(self, obj):
        return obj.calculate_ctc()

    ctc_display.short_description = 'CTC (Cost to Company)'

admin.site.register(EmployeeCTC, EmployeeCTCAdmin)
