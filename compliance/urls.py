from django.contrib import admin
from django.urls import path,include
from . import views


from django.urls import path
from . import views

urlpatterns = [
    path('add_employee/', views.add_employee, name='add_employee'),
    path('employee_success/', views.employee_success, name='employee_success'),  # You can add a success view

    path('compliance/applicant/', views.applicant_compliance_view, name='applicant_compliance'),
]
