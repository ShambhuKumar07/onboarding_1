 
from django.urls import path
from django.views.generic import TemplateView  # Import TemplateView

from .views import employee_ctc_view,applicant_compensation_view

# urlpatterns = [
#     path('compensation/employee/ctc/', employee_ctc_view, name='employee_ctc'),
#     path('success/', TemplateView.as_view(template_name='compensation/success.html'), name='success_page'),

#     path('compensation/applicant/', applicant_compensation_view, name='applicant_compensation'),
# ]



from django.urls import path
from .views import employee_ctc_view, applicant_compensation_view, import_employee_ctc_view

urlpatterns = [
    path('compensation/employee/ctc/', employee_ctc_view, name='employee_ctc'),
    path('compensation/import/', import_employee_ctc_view, name='import_employee_ctc'),  # Add import URL
    path('success/', TemplateView.as_view(template_name='compensation/success.html'), name='success_page'),
    path('compensation/applicant/', applicant_compensation_view, name='applicant_compensation'),
]
