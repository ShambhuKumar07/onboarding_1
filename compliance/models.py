#compliance/models.py

from django.db import models
from applicant.models import Applicant  # Assuming compliance is linked to an applicant
from users.models import Profile  # Import the Profile model
from compensation.models import EmployeeCTC
# Create your models here.

class Employee(models.Model):
    # applicant = models.ForeignKey(Applicant, null=True, blank=True, on_delete=models.CASCADE)  # Allow null
    applicant = models.OneToOneField(Applicant, on_delete=models.CASCADE, default=1)  # Set a valid default Applicant ID here
    profile = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)  # Add ForeignKey to Profile
    uan_number = models.CharField(max_length=12, unique=True, verbose_name="UAN No.")
    pan_number = models.CharField(max_length=10, unique=True, verbose_name="PAN No.")
    esic_number = models.CharField(max_length=17, unique=True, verbose_name="ESIC No.")

    def __str__(self):
        return f"{self.pan_number} - {self.uan_number}"

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        ordering = ['pan_number']  # Optional: Orders by PAN No.
