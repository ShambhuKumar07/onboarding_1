from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from onboarding.models import Onboarding, OnboardingTasks
from django.utils import timezone
import datetime
from django.db.models import Q
from users.models import Profile

@login_required
def main_page(request):
    if not request.user.is_staff:
        return main_page_user(request)

    today = timezone.now()
    active_onboardings = Onboarding.objects.filter(entry_date__gte=today)
    past_due_tasks = OnboardingTasks.objects.filter(Q(state='ST') | Q(state='PR'), date_due__lt=today)[:10]
    tasks_due_week = OnboardingTasks.objects.filter(date_due__lt=today + datetime.timedelta(days=7),date_due__gte=today)[:10] 
    task_updated_last_week = OnboardingTasks.objects.filter(last_updated__lte=today).order_by('-last_updated')[:10]

    context = {
        'active_onboardings':active_onboardings,
        'past_due_tasks':past_due_tasks,
        'tasks_due_week':tasks_due_week,
        'task_updated_last_week':task_updated_last_week,
        'today':today
    }
    
    if request.user.is_staff:
        context['selected_profile'] = Profile.objects.first()  # Or get a specific profile
    

    return render(request,'core/main.html',context)

# from django.shortcuts import render
# from users.models import Profile
# from django.db.models import Count
# from datetime import date
# from dateutil.relativedelta import relativedelta

# def main_page(request):
#     # Gender data
#     gender_data = Profile.objects.values('gender').annotate(count=Count('gender'))

#     # Age data
#     today = date.today()
#     age_ranges = [
#         {"label": "20-30", "min_age": 20, "max_age": 30},
#         {"label": "30-40", "min_age": 30, "max_age": 40},
#         {"label": "40-50", "min_age": 40, "max_age": 50},
#     ]
#     age_data = []
#     for age_range in age_ranges:
#         min_date = today - relativedelta(years=age_range['max_age'])
#         max_date = today - relativedelta(years=age_range['min_age'])
#         count = Profile.objects.filter(date_of_birth__range=(min_date, max_date)).count()
#         age_data.append({"label": age_range['label'], "count": count})

#     # Hires and attrition
#     current_year = today.year
#     hire_data = Profile.objects.filter(date_of_joining__year=current_year).count()
#     attrition_data = Profile.objects.filter(end_date__year=current_year).count()

#     context = {
#         'gender_data': list(gender_data),
#         'age_data': age_data,
#         'hire_data': hire_data,
#         'attrition_data': attrition_data,
#     }

#     return render(request, 'core/main.html', context)




def main_page_user(request):
    today = timezone.now()
    tasks_due = OnboardingTasks.objects.filter(Q(date_due__gte=today) | Q(date_due=None),assigned_to=request.user).exclude(state=OnboardingTasks.COMPLETED)
    tasks_completed = OnboardingTasks.objects.filter(state=OnboardingTasks.COMPLETED, assigned_to=request.user).order_by('-date_due')[:10]

    context = {
        'tasks_due':tasks_due,
        'tasks_completed':tasks_completed
    }
    return render(request,'core/main_user.html',context)

