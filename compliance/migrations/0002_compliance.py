# Generated by Django 5.0.4 on 2024-10-16 11:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("applicant", "0006_applicant_profile"),
        ("compliance", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Compliance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uan_number",
                    models.CharField(
                        max_length=12, unique=True, verbose_name="UAN No."
                    ),
                ),
                (
                    "pan_number",
                    models.CharField(
                        max_length=10, unique=True, verbose_name="PAN No."
                    ),
                ),
                (
                    "esic_number",
                    models.CharField(
                        max_length=17, unique=True, verbose_name="ESIC No."
                    ),
                ),
                (
                    "applicant",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="compliance",
                        to="applicant.applicant",
                    ),
                ),
            ],
            options={
                "verbose_name": "Compliance",
                "verbose_name_plural": "Compliance Records",
            },
        ),
    ]
