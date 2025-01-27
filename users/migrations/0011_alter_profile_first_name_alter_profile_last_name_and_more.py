# Generated by Django 5.0.4 on 2024-09-24 05:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0010_employmentrecord_document"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="first_name",
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="profile",
            name="last_name",
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="profile",
            name="middle_name",
            field=models.CharField(blank=True, default=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="short_code",
            field=models.CharField(max_length=13, null=True, unique=True),
        ),
    ]
