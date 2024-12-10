#users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from image_cropping import ImageRatioField  
from datetime import date

class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

class Profile(models.Model):
    MALE = 'ML'
    FEMALE = 'FM'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    
    first_name = models.CharField(max_length=100, default=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True, default=False)
    last_name = models.CharField(max_length=100, default=True)
    employee_code = models.CharField(max_length=13, null=True, unique=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    date_of_joining = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)  # Add this line
    email = models.EmailField(null=True)
    user = models.OneToOneField(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="profile_pics", null=True, blank=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE)
    cropping = ImageRatioField('picture', '300x300')
    father_name = models.CharField(max_length=100, null=True, blank=True)
    mother_name = models.CharField(max_length=100, null=True, blank=True)
    blood_group = models.CharField(max_length=3, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    present_address = models.TextField(null=True, blank=True)
    permanent_address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    personal_email = models.EmailField(null=True, blank=True)
    pan_number = models.CharField(max_length=10, null=True, blank=True)
    marital_status = models.CharField(max_length=50, null=True, blank=True)
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    ifsc_code = models.CharField(max_length=20, null=True, blank=True)
    bank_account_number = models.CharField(max_length=20, null=True, blank=True)
    emergency_contact_name = models.CharField(max_length=100, null=True, blank=True)
    emergency_contact_relation = models.CharField(max_length=100, null=True, blank=True)
    emergency_contact_number = models.CharField(max_length=20, null=True, blank=True)

    @property
    def fullname(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'
    
    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
        return None

    @property
    def gender_label(self):
        return dict(self.GENDER_CHOICES).get(self.gender, "Unknown")

class FamilyMember(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='family_members')
    relation = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=10)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name} ({self.relation})'

class EducationalQualification(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='educational_qualifications')
     

    examination_passed = models.CharField(max_length=255)
    year_of_passing = models.IntegerField()
    school_or_college = models.CharField(max_length=255)
    subjects = models.TextField()
    division = models.CharField(max_length=50)
    document = models.FileField(upload_to='qualifications/', blank=True, null=True)

    def __str__(self):
        return f'{self.examination_passed} - {self.year_of_passing}'

class EmploymentRecord(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='employment_records')
    
    organization = models.CharField(max_length=255)
    designation = models.CharField(max_length=100)
    joining_date = models.DateField()
    leaving_date = models.DateField()
    document = models.FileField(upload_to='employment_documents/', blank=True, null=True)

    def __str__(self):
        return f'{self.organization} - {self.designation}'

class LanguageProficiency(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='languages')
    language = models.CharField(max_length=50)
    speak = models.CharField(max_length=1, choices=[('A', 'Fluent'), ('B', 'Fair'), ('C', 'Workable')])
    read = models.CharField(max_length=1, choices=[('A', 'Fluent'), ('B', 'Fair'), ('C', 'Workable')])
    write = models.CharField(max_length=1, choices=[('A', 'Fluent'), ('B', 'Fair'), ('C', 'Workable')])

    def __str__(self):
        return self.language

class Reference(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='references')
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
