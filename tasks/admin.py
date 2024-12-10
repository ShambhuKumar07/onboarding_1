# from django.contrib import admin
# from . import models
# # Register your models here.

# @admin.register(models.Task)
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('title','category','date_due')
#     list_filter = ('category','date_due')


# @admin.register(models.TaskCategory)
# class TaskCategoryAdmin(admin.ModelAdmin):
#     pass


# tasks/admin.py
from django.contrib import admin
from .models import Task, TaskCategory

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_due')
    search_fields = ('title', 'category__title', 'description')
    list_filter = ('date_due', 'category')

@admin.register(TaskCategory)
class TaskCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
