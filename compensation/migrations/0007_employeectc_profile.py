# Generated by Django 5.0.4 on 2024-10-22 06:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("compensation", "0006_delete_compliance"),
        ("users", "0013_educationalqualification_document"),
    ]

    operations = [
        migrations.AddField(
            model_name="employeectc",
            name="profile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.profile",
            ),
        ),
    ]
