# Generated by Django 2.2.2 on 2019-06-05 08:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0003_auto_20190530_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onboardingtasks',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
