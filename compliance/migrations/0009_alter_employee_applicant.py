# Generated by Django 5.0.4 on 2024-10-18 05:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("applicant", "0006_applicant_profile"),
        ("compliance", "0008_alter_employee_applicant"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="applicant",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="applicant.applicant",
            ),
        ),
    ]