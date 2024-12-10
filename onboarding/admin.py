from django.contrib import admin
from . import models
from .forms import OnboardingAdminForm

class ContractInline(admin.TabularInline):
    model = models.Contract 


class NewEmployeeInline(admin.TabularInline):
    model = models.NewEmployee
    extra = 1
    min_num = 1
    readonly_fields = ('work_email',)

class OnboardingTasksInline(admin.StackedInline):
    model = models.OnboardingTasks
    extra = 1
    ordering = ('position',)


@admin.register(models.Onboarding)
class OnboardingAdmin(admin.ModelAdmin):
    inlines = [NewEmployeeInline,ContractInline,OnboardingTasksInline]
    list_display = ('__str__','entry_date') 
    
    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.inlines = ([NewEmployeeInline,ContractInline,OnboardingTasksInline])
        return super().change_view(request, object_id, form_url=form_url, extra_context=extra_context)

    def add_view(self, request, form_url='', extra_context=None):
        self.inlines = ([NewEmployeeInline,ContractInline])
        return super().add_view(request, form_url=form_url, extra_context=extra_context)
    
    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            kwargs['form'] = OnboardingAdminForm
        return super().get_form(request, obj, **kwargs)

    def save_form(self, request, form, change):
        return super().save_form(request, form, change)   

    def save_model(self, request, obj, form, change):
        template = form.cleaned_data.get('template',None)
        super().save_model(request, obj, form, change)
        if template and obj:
        # copy all tasks with position to taskstemplate
            for task_temp in template.templatetasks_set.all():
                test = models.OnboardingTasks.objects.create(task=task_temp.task,onboarding=obj,position=task_temp.position)
                

@admin.register(models.OnboardingTasks)
class OnboardingTasksAdmin(admin.ModelAdmin):
    list_display = ('onboarding','task','position','state','assigned_to','date_due')
    ordering = ('onboarding','position')
    list_filter = ('onboarding__newemployee__profile__last_name','state','assigned_to__username')






########################################################

# onboarding/admin.py
# from django.contrib import admin
# from .models import Onboarding, NewEmployee, Contract, OnboardingTasks

# @admin.register(Onboarding)
# class OnboardingAdmin(admin.ModelAdmin):
#     list_display = (
#         'entry_date',
#         'trial_period',
#         'newemployee',
#         'tasks_to_complete',
#     )
#     search_fields = (
#         'newemployee__profile__first_name',
#         'newemployee__profile__last_name',
#         'newemployee__personal_email',
#     )
#     list_filter = ('entry_date', 'trial_period')

# @admin.register(NewEmployee)
# class NewEmployeeAdmin(admin.ModelAdmin):
#     list_display = ('profile', 'birth_date', 'personal_email', 'onboarding')
#     search_fields = (
#         'profile__first_name',
#         'profile__last_name',
#         'personal_email',
#     )
#     list_filter = ('birth_date',)

# @admin.register(Contract)
# class ContractAdmin(admin.ModelAdmin):
#     list_display = ('contract_nr', 'onboarding', 'salary', 'work_time')
#     search_fields = ('contract_nr', 'onboarding__newemployee__profile__first_name')
#     list_filter = ('work_time',)

# @admin.register(OnboardingTasks)
# class OnboardingTasksAdmin(admin.ModelAdmin):
#     list_display = (
#         'task',
#         'onboarding',
#         'state',
#         'assigned_to',
#         'date_due',
#         'last_updated',
#     )
#     search_fields = (
#         'task__title',
#         'onboarding__newemployee__profile__first_name',
#         'assigned_to__username',
#     )
#     list_filter = ('state', 'date_due', 'assigned_to')
