# Generated by Django 5.0.4 on 2024-12-04 10:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0015_profile_end_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="Employee_Code",
            new_name="employee_code",
        ),
    ]
