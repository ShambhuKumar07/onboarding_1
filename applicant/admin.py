# applicant/admin.py
from django.contrib import admin
from .models import Applicant

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address', 'applied_on')
    search_fields = ('user__username', 'phone', 'address')
    list_filter = ('applied_on',)


