# from django.contrib import admin
# from . import models


# # Inlines


# class TemplateTasksInline(admin.TabularInline):
#     model = models.TemplateTasks
#     extra = 0
#     ordering = ('position',)



# @admin.register(models.OnboardingTemplate)
# class OnboardingTemplateAdmin(admin.ModelAdmin):
#     inlines = (TemplateTasksInline,)


# core/admin.py
from django.contrib import admin
from .models import OnboardingTemplate, TemplateTasks

@admin.register(OnboardingTemplate)
class OnboardingTemplateAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')

@admin.register(TemplateTasks)
class TemplateTasksAdmin(admin.ModelAdmin):
    list_display = ('onboardingTemplate', 'task', 'position')
    search_fields = (
        'onboardingTemplate__title',
        'task__title',
    )
    list_filter = ('onboardingTemplate',)




