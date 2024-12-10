from django.apps import AppConfig


class ApplicantConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "applicant"

# applicant/apps.py

# from django.apps import AppConfig

# class ApplicantConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'applicant'

#     def ready(self):
#         # Import the signals to ensure they are registered
#         import applicant.signals
