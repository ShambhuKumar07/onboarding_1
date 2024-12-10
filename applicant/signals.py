# applicant/signals.py

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from compliance.models import Compliance
# from .models import Applicant  # Import the Applicant model

# # This signal is triggered after an Applicant is saved
# @receiver(post_save, sender=Applicant)
# def create_compliance(sender, instance, created, **kwargs):
#     # Only create a Compliance record when a new Applicant is created
#     if created:
#         Compliance.objects.create(applicant=instance)
