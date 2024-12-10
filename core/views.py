from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from onboarding.models import Onboarding, OnboardingTasks
from users.models import Profile
from django.utils import timezone
from django.db.models import Count, Q
from django.db.models.functions import ExtractYear, ExtractMonth
from django.db.models.functions import TruncMonth, ExtractYear, ExtractMonth
from datetime import timedelta
import json
from collections import defaultdict



# # @login_required
# # def main_page(request):
# #     if not request.user.is_staff:
# #         return main_page_user(request)

# #     today = timezone.now()
# #     # Gender data
# #     gender_data = Profile.objects.values('gender').annotate(count=Count('gender'))
# #     # Age data
# #     age_ranges = [
# #         {"label": "20-30", "min_age": 20, "max_age": 30},
# #         {"label": "30-40", "min_age": 30, "max_age": 40},
# #         {"label": "40-50", "min_age": 40, "max_age": 50},
# #     ]
# #     age_data = []
# #     for age_range in age_ranges:
# #         min_date = today - relativedelta(years=age_range['max_age'])
# #         max_date = today - relativedelta(years=age_range['min_age'])
# #         count = Profile.objects.filter(date_of_birth__range=(min_date, max_date)).count()
# #         age_data.append({"label": age_range['label'], "count": count})

# #     # Other context
# #     active_onboardings = Onboarding.objects.filter(entry_date__gte=today)
# #     past_due_tasks = OnboardingTasks.objects.filter(Q(state='ST') | Q(state='PR'), date_due__lt=today)[:10]
# #     tasks_due_week = OnboardingTasks.objects.filter(date_due__lt=today + timedelta(days=7), date_due__gte=today)[:10]

# #     context = {
# #         'gender_data': list(gender_data),
# #         'age_data': age_data,
# #         'active_onboardings': active_onboardings,
# #         'past_due_tasks': past_due_tasks,
# #         'tasks_due_week': tasks_due_week,
# #     }

# #     return render(request, 'core/main.html', context)







# # import json
# # from django.http import JsonResponse

# # @login_required
# # def main_page(request):
# #     if not request.user.is_staff:
# #         return main_page_user(request)

# #     today = timezone.now()
# #     # Gender data
# #     gender_data = Profile.objects.values('gender').annotate(count=Count('gender'))
# #     # Age data
# #     age_ranges = [
# #         {"label": "20-30", "min_age": 20, "max_age": 30},
# #         {"label": "30-40", "min_age": 30, "max_age": 40},
# #         {"label": "40-50", "min_age": 40, "max_age": 50},
# #     ]
# #     age_data = []
# #     for age_range in age_ranges:
# #         min_date = today - relativedelta(years=age_range['max_age'])
# #         max_date = today - relativedelta(years=age_range['min_age'])
# #         count = Profile.objects.filter(date_of_birth__range=(min_date, max_date)).count()
# #         age_data.append({"label": age_range['label'], "count": count})

# #     # Debug data
# #     print("Gender Data:", gender_data)
# #     print("Age Data:", age_data)

# #     # Other context
# #     active_onboardings = Onboarding.objects.filter(entry_date__gte=today)
# #     past_due_tasks = OnboardingTasks.objects.filter(Q(state='ST') | Q(state='PR'), date_due__lt=today)[:10]
# #     tasks_due_week = OnboardingTasks.objects.filter(date_due__lt=today + timedelta(days=7), date_due__gte=today)[:10]

# #     context = {
# #         'gender_data': list(gender_data),
# #         'age_data': age_data,
# #         'active_onboardings': active_onboardings,
# #         'past_due_tasks': past_due_tasks,
# #         'tasks_due_week': tasks_due_week,
# #     }

# #     return render(request, 'core/main.html', context)

# import json
# from applicant.models import Applicant

# @login_required
# def main_page(request):
#     if not request.user.is_staff:
#         return main_page_user(request)

#     today = timezone.now()
    
#     # Filter only applicants
#     applicant_profiles = Profile.objects.filter(applicant__isnull=False)
#     for profile in applicant_profiles:
#         print(profile.fullname, profile.date_of_birth, profile.gender)

#     # Gender data
#     gender_data = applicant_profiles.values('gender').annotate(count=Count('gender'))

#     # Age data
#     age_ranges = [
#         {"label": "20-30", "min_age": 20, "max_age": 30},
#         {"label": "30-40", "min_age": 30, "max_age": 40},
#         {"label": "40-50", "min_age": 40, "max_age": 50},
#     ]
#     age_data = []
#     for age_range in age_ranges:
#         min_date = today - relativedelta(years=age_range['max_age'])
#         max_date = today - relativedelta(years=age_range['min_age'])
#         count = applicant_profiles.filter(date_of_birth__range=(min_date, max_date)).count()
#         age_data.append({"label": age_range['label'], "count": count})

#     # Debug data
#     print("Gender Data:", gender_data)
#     print("Age Data:", age_data)

#     # Other context
#     active_onboardings = Onboarding.objects.filter(entry_date__gte=today)
#     past_due_tasks = OnboardingTasks.objects.filter(Q(state='ST') | Q(state='PR'), date_due__lt=today)[:10]
#     tasks_due_week = OnboardingTasks.objects.filter(date_due__lt=today + timedelta(days=7), date_due__gte=today)[:10]

#     context = {
#     # 'gender_data': list(gender_data),
#     'gender_data':json.dumps(list(gender_data)),
#     # 'age_data': age_data,
#     'age_data': json.dumps(age_data),
#     'active_onboardings': active_onboardings,
#     'past_due_tasks': past_due_tasks,
#     'tasks_due_week': tasks_due_week,
#     }
#     print("Context Data:", context)

#     return render(request, 'core/main.html', context)




# def main_page_user(request):
#     today = timezone.now()
#     tasks_due = OnboardingTasks.objects.filter(Q(date_due__gte=today) | Q(date_due=None), assigned_to=request.user).exclude(state=OnboardingTasks.COMPLETED)
#     tasks_completed = OnboardingTasks.objects.filter(state=OnboardingTasks.COMPLETED, assigned_to=request.user).order_by('-date_due')[:10]

#     context = {
#         'tasks_due': tasks_due,
#         'tasks_completed': tasks_completed,
#     }
#     return render(request, 'core/main_user.html', context)


# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from onboarding.models import Onboarding, OnboardingTasks
# from django.utils import timezone
# from django.db.models import Count, Q
# from datetime import timedelta
# from dateutil.relativedelta import relativedelta
# from users.models import Profile
# import json


########################## Age and Gender 

# @login_required
# def main_page(request):
#     if not request.user.is_staff:
#         return main_page_user(request)

#     today = timezone.now()

#     # Filter only applicant profiles
#     applicant_profiles = Profile.objects.filter(applicant__isnull=False)

#     # for profile in applicant_profiles:
#     #     print(f"Profile: {profile.fullname}, Age: {getattr(profile, 'age', 'Not Found')}, DOB: {profile.date_of_birth}")

#     # Gender data
#     gender_data = applicant_profiles.values('gender').annotate(count=Count('gender'))

#     # Age data
#     age_ranges = [
#         {"label": "20-30", "min_age": 20, "max_age": 30},
#         {"label": "30-40", "min_age": 30, "max_age": 40},
#         {"label": "40-50", "min_age": 40, "max_age": 50},
#     ]
#     age_data = []
#     for age_range in age_ranges:
#         count = sum(
#             1
#             for profile in applicant_profiles
#             if profile.age and age_range["min_age"] <= profile.age < age_range["max_age"]
#         )
#         age_data.append({"label": age_range["label"], "count": count})

#     # Debugging logs
#     # print("Gender Data:", gender_data)
#     # print("Age Data:", age_data)

#     # Other context
#     active_onboardings = Onboarding.objects.filter(entry_date__gte=today)
#     past_due_tasks = OnboardingTasks.objects.filter(Q(state='ST') | Q(state='PR'), date_due__lt=today)[:10]
#     tasks_due_week = OnboardingTasks.objects.filter(date_due__lt=today + timedelta(days=7), date_due__gte=today)[:10]

#     context = {
#     'gender_data': json.dumps(list(gender_data)),  # Serialize queryset to JSON
#     'age_data': json.dumps(age_data),             # Serialize list to JSON
#     'active_onboardings': active_onboardings,
#     'past_due_tasks': past_due_tasks,
#     'tasks_due_week': tasks_due_week,
# }

#     return render(request, 'core/main.html', context)



################## Age, Gender and Attrition






# @login_required
# def main_page(request):
#     if not request.user.is_staff:
#         return main_page_user(request)

#     today = timezone.now()

#     # Filter applicant profiles
#     applicant_profiles = Profile.objects.filter(applicant__isnull=False)

#     # Gender data
#     gender_data = applicant_profiles.values('gender').annotate(count=Count('gender'))

#     # Age data
#     age_ranges = [
#         {"label": "20-30", "min_age": 20, "max_age": 30},
#         {"label": "30-40", "min_age": 30, "max_age": 40},
#         {"label": "40-50", "min_age": 40, "max_age": 50},
#     ]
#     age_data = []
#     for age_range in age_ranges:
#         count = sum(
#             1
#             for profile in applicant_profiles
#             if profile.age and age_range["min_age"] <= profile.age < age_range["max_age"]
#         )
#         age_data.append({"label": age_range["label"], "count": count})

#     # Attrition data
#     attrition_profiles = Profile.objects.filter(end_date__isnull=False)



#     # Attrition data (per year)
#     attrition_data = (
#     Profile.objects.filter(end_date__isnull=False)
#     .annotate(year=TruncMonth('end_date'))
#     .values('year')
#     .annotate(count=Count('id'))
#     .order_by('year')
#     )

#     #   Transform attrition data to match the chart format
#     attrition_data_chart = [
#     {"year": item['year'].year, "count": item['count']}
#     for item in attrition_data
#     ]

#     # Prepare context with updated attrition data
 

#     # attrition_data = [
#     #     {"label": "Attrition", "count": attrition_profiles.count()},
#     #     {"label": "Active", "count": applicant_profiles.count() - attrition_profiles.count()},
#     # ]


    

    


#     # Hiring data by month
#     hiring_data = (
#         Profile.objects.filter(date_of_joining__isnull=False)
#         .annotate(month=TruncMonth('date_of_joining'))
#         .values('month')
#         .annotate(count=Count('id'))
#         .order_by('month')
#     )

#     # Transform hiring data for the chart
#     hiring_data_chart = [
#         {"label": month['month'].strftime('%B %Y'), "count": month['count']}
#         for month in hiring_data
#     ]


#     # Other context
#     active_onboardings = Onboarding.objects.filter(entry_date__gte=today)
#     past_due_tasks = OnboardingTasks.objects.filter(Q(state='ST') | Q(state='PR'), date_due__lt=today)[:10]
#     tasks_due_week = OnboardingTasks.objects.filter(date_due__lt=today + timedelta(days=7), date_due__gte=today)[:10]

#     context = {
#         'gender_data': json.dumps(list(gender_data)),
#         'age_data': json.dumps(age_data),
#         'attrition_data': json.dumps(attrition_data),  # Serialize attrition data to JSON
#         'hiring_data_chart': json.dumps(hiring_data_chart),
#         'active_onboardings': active_onboardings,
#         'past_due_tasks': past_due_tasks,
#         'tasks_due_week': tasks_due_week,
#     }

#     return render(request, 'core/main.html', context)




###################################




# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from onboarding.models import Onboarding, OnboardingTasks
# from django.utils import timezone
# from django.db.models import Count, Q
# from datetime import timedelta
# from dateutil.relativedelta import relativedelta
# from users.models import Profile
# import json
# from django.db.models.functions import TruncMonth


# from django.db.models import Count
# from collections import defaultdict


# @login_required
# def main_page(request):
#     if not request.user.is_staff:
#         return main_page_user(request)

#     today = timezone.now()

#     # Filter applicant profiles
#     applicant_profiles = Profile.objects.filter(applicant__isnull=False)

#     # Gender data
#     gender_data = list(applicant_profiles.values('gender').annotate(count=Count('gender')))

#     # Age data
#     age_ranges = [
#         {"label": "20-30", "min_age": 20, "max_age": 30},
#         {"label": "30-40", "min_age": 30, "max_age": 40},
#         {"label": "40-50", "min_age": 40, "max_age": 50},
#     ]
#     age_data = []
#     for age_range in age_ranges:
#         count = sum(
#             1
#             for profile in applicant_profiles
#             if profile.age and age_range["min_age"] <= profile.age < age_range["max_age"]
#         )
#         age_data.append({"label": age_range["label"], "count": count})

#     # # Attrition data
#     # attrition_data = list(
#     #     Profile.objects.filter(end_date__isnull=False)
#     #     .annotate(year=TruncMonth('end_date'))
#     #     .values('year')
#     #     .annotate(count=Count('id'))
#     #     .order_by('year')
#     # )

#     # # Transform attrition data to match the chart format
#     # attrition_data_chart = [
#     #     {"year": item['year'].year, "count": item['count']}
#     #     for item in attrition_data
#     # ]


#     from collections import defaultdict

# # Attrition data grouped by year and month
#     attrition_data = Profile.objects.filter(end_date__isnull=False).annotate(
#         year=TruncMonth('end_date').year,
#         month=TruncMonth('end_date').month,
#     ).values('year', 'month').annotate(count=Count('id')).order_by('year', 'month')

# # Generate a dictionary with year and month as keys
#     attrition_dict = defaultdict(lambda: [0] * 12)  # Default for each year is a list of 12 zeros
#     for item in attrition_data:
#         attrition_dict[item['year']][item['month'] - 1] = item['count']  # Subtract 1 for zero-indexed months

# # Transform to a chart-compatible format
#     attrition_data_chart = {
#         "years": list(attrition_dict.keys()),
#         "data": list(attrition_dict.values()),
#     }


#     # Hiring data by month
#     hiring_data = (
#         Profile.objects.filter(date_of_joining__isnull=False)
#         .annotate(month=TruncMonth('date_of_joining'))
#         .values('month')
#         .annotate(count=Count('id'))
#         .order_by('month')
#     )

#     # Transform hiring data for the chart
#     hiring_data_chart = [
#         {"label": month['month'].strftime('%B %Y'), "count": month['count']}
#         for month in hiring_data
#     ]

#     # Other context
#     active_onboardings = Onboarding.objects.filter(entry_date__gte=today)
#     past_due_tasks = OnboardingTasks.objects.filter(Q(state='ST') | Q(state='PR'), date_due__lt=today)[:10]
#     tasks_due_week = OnboardingTasks.objects.filter(date_due__lt=today + timedelta(days=7), date_due__gte=today)[:10]

#     context = {
#         'gender_data': json.dumps(gender_data),
#         'age_data': json.dumps(age_data),
#         'attrition_data': json.dumps(attrition_data_chart),
#         'hiring_data_chart': json.dumps(hiring_data_chart),
#         'active_onboardings': active_onboardings,
#         'past_due_tasks': past_due_tasks,
#         'tasks_due_week': tasks_due_week,
#     }

#     return render(request, 'core/main.html', context)


#########################################

# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from onboarding.models import Onboarding, OnboardingTasks
# from users.models import Profile
# from django.utils import timezone
# from django.db.models import Count, Q

# from datetime import timedelta
# import json
# from collections import defaultdict

# # Helper Functions
# def get_gender_data(applicant_profiles):
#     """Get gender distribution data."""
#     return list(applicant_profiles.values('gender').annotate(count=Count('gender')))

# def get_age_data(applicant_profiles):
#     """Get age distribution data."""
#     age_ranges = [
#         {"label": "20-30", "min_age": 20, "max_age": 30},
#         {"label": "30-40", "min_age": 30, "max_age": 40},
#         {"label": "40-50", "min_age": 40, "max_age": 50},
#     ]
#     age_data = []
#     for age_range in age_ranges:
#         count = sum(
#             1
#             for profile in applicant_profiles
#             if profile.age and age_range["min_age"] <= profile.age < age_range["max_age"]
#         )
#         age_data.append({"label": age_range["label"], "count": count})
#     return age_data

# def get_attrition_data():
#     """Get attrition data grouped by year and month."""
#     attrition_data = Profile.objects.filter(end_date__isnull=False).annotate(
#         year=ExtractYear('end_date'),
#         month=ExtractMonth('end_date')
#     ).values('year', 'month').annotate(count=Count('id')).order_by('year', 'month')

#     attrition_dict = defaultdict(lambda: [0] * 12)
#     for item in attrition_data:
#         attrition_dict[item['year']][item['month'] - 1] = item['count']

#     return {
#         "years": list(attrition_dict.keys()),
#         "data": list(attrition_dict.values()),
#     }

# def get_hiring_data():
#     """Get hiring data grouped by month."""
#     hiring_data = (
#         Profile.objects.filter(date_of_joining__isnull=False)
#         .annotate(month=TruncMonth('date_of_joining'))
#         .values('month')
#         .annotate(count=Count('id'))
#         .order_by('month')
#     )
#     return [
#         {"label": month['month'].strftime('%B %Y'), "count": month['count']}
#         for month in hiring_data
#     ]

# def get_task_data(today):
#     """Get task data for active, past due, and due this week."""
#     active_onboardings = Onboarding.objects.filter(entry_date__gte=today)
#     past_due_tasks = OnboardingTasks.objects.filter(
#         Q(state='ST') | Q(state='PR'), date_due__lt=today
#     )[:10]
#     tasks_due_week = OnboardingTasks.objects.filter(
#         date_due__lt=today + timedelta(days=7), date_due__gte=today
#     )[:10]
#     return active_onboardings, past_due_tasks, tasks_due_week

# # Main View
# @login_required
# def main_page(request):
#     if not request.user.is_staff:
#         return main_page_user(request)

#     today = timezone.now()
#     applicant_profiles = Profile.objects.filter(applicant__isnull=False)

#     # Get chart data
#     gender_data = get_gender_data(applicant_profiles)
#     age_data = get_age_data(applicant_profiles)
#     attrition_data = get_attrition_data()
#     hiring_data_chart = get_hiring_data()

#     # Get task data
#     active_onboardings, past_due_tasks, tasks_due_week = get_task_data(today)

#     # Context for rendering
#     context = {
#         'gender_data': json.dumps(gender_data),
#         'age_data': json.dumps(age_data),
#         'attrition_data': json.dumps(attrition_data),
#         'hiring_data_chart': json.dumps(hiring_data_chart),
#         'active_onboardings': active_onboardings,
#         'past_due_tasks': past_due_tasks,
#         'tasks_due_week': tasks_due_week,
#     }

#     return render(request, 'core/main.html', context)



############################# Attrition Report #####################





# # Helper Functions
# def get_gender_data(applicant_profiles):
#     return list(applicant_profiles.values('gender').annotate(count=Count('gender')))

# def get_age_data(applicant_profiles):
#     age_ranges = [
#         {"label": "20-30", "min_age": 20, "max_age": 30},
#         {"label": "30-40", "min_age": 30, "max_age": 40},
#         {"label": "40-50", "min_age": 40, "max_age": 50},
#     ]
#     age_data = []
#     for age_range in age_ranges:
#         count = sum(
#             1
#             for profile in applicant_profiles
#             if profile.age and age_range["min_age"] <= profile.age < age_range["max_age"]
#         )
#         age_data.append({"label": age_range["label"], "count": count})
#     return age_data

# # def get_attrition_da

# from datetime import datetime

# def get_attrition_data():
#     """
#     Get attrition data grouped by year and month.
#     """
#     attrition_data = Profile.objects.filter(end_date__isnull=False).annotate(
#         year=ExtractYear('end_date'),
#         month=ExtractMonth('end_date')
#     ).values('year', 'month').annotate(count=Count('id')).order_by('year', 'month')

#     # Generate a dictionary for attrition counts by year and month
#     attrition_dict = defaultdict(lambda: [0] * 12)  # Default is a list of 12 zeros for each year
#     for item in attrition_data:
#         attrition_dict[item['year']][item['month'] - 1] = item['count']  # Zero-indexed months

#     # Ensure years from 2008 to current year are included
#     current_year = datetime.now().year
#     all_years = list(range(2008, current_year + 1))
#     for year in all_years:
#         if year not in attrition_dict:
#             attrition_dict[year] = [0] * 12

#     # Prepare the chart data format
#     return {
#         "years": all_years,  # All years from 2008 to now
#         "data": attrition_dict,
#     }

# def get_hiring_data():
#     hiring_data = (
#         Profile.objects.filter(date_of_joining__isnull=False)
#         .annotate(month=TruncMonth('date_of_joining'))
#         .values('month')
#         .annotate(count=Count('id'))
#         .order_by('month')
#     )
#     return [
#         {"label": month['month'].strftime('%B %Y'), "count": month['count']}
#         for month in hiring_data
#     ]

# def get_task_data(today):
#     active_onboardings = Onboarding.objects.filter(entry_date__gte=today)
#     past_due_tasks = OnboardingTasks.objects.filter(
#         Q(state='ST') | Q(state='PR'), date_due__lt=today
#     )[:10]
#     tasks_due_week = OnboardingTasks.objects.filter(
#         date_due__lt=today + timedelta(days=7), date_due__gte=today
#     )[:10]
#     return active_onboardings, past_due_tasks, tasks_due_week

# # Main View
# @login_required
# def main_page(request):
#     if not request.user.is_staff:
#         return main_page_user(request)

#     today = timezone.now()
#     applicant_profiles = Profile.objects.filter(applicant__isnull=False)

#     # Get chart data
#     gender_data = get_gender_data(applicant_profiles)
#     age_data = get_age_data(applicant_profiles)
#     attrition_data = get_attrition_data()
#     hiring_data_chart = get_hiring_data()

#     # Get task data
#     active_onboardings, past_due_tasks, tasks_due_week = get_task_data(today)

#     # Context for rendering
#     context = {
#     'gender_data': json.dumps(gender_data),
#     'age_data': json.dumps(age_data),
#     'attrition_data': json.dumps(attrition_data),  # Keep full data for the chart
#     'attrition_years': attrition_data['years'],   # Pass years separately for the dropdown
#     'hiring_data_chart': json.dumps(hiring_data_chart),
#     'active_onboardings': active_onboardings,
#     'past_due_tasks': past_due_tasks,
#     'tasks_due_week': tasks_due_week,
#     }
 
#     return render(request, 'core/main.html', context)




############################# Hiring Report ##############


from collections import defaultdict
from datetime import datetime


# Helper Functions
def get_gender_data(applicant_profiles):
    return list(applicant_profiles.values('gender').annotate(count=Count('gender')))

def get_age_data(applicant_profiles):
    age_ranges = [
        {"label": "20-30", "min_age": 20, "max_age": 30},
        {"label": "30-40", "min_age": 30, "max_age": 40},
        {"label": "40-50", "min_age": 40, "max_age": 50},
    ]
    age_data = []
    for age_range in age_ranges:
        count = sum(
            1
            for profile in applicant_profiles
            if profile.age and age_range["min_age"] <= profile.age < age_range["max_age"]
        )
        age_data.append({"label": age_range["label"], "count": count})
    return age_data

# def get_attrition_da

from datetime import datetime

def get_attrition_data():
    """
    Get attrition data grouped by year and month.
    """
    attrition_data = Profile.objects.filter(end_date__isnull=False).annotate(
        year=ExtractYear('end_date'),
        month=ExtractMonth('end_date')
    ).values('year', 'month').annotate(count=Count('id')).order_by('year', 'month')

    # Generate a dictionary for attrition counts by year and month
    attrition_dict = defaultdict(lambda: [0] * 12)  # Default is a list of 12 zeros for each year
    for item in attrition_data:
        attrition_dict[item['year']][item['month'] - 1] = item['count']  # Zero-indexed months

    # Ensure years from 2008 to current year are included
    current_year = datetime.now().year
    all_years = list(range(2008, current_year + 1))
    for year in all_years:
        if year not in attrition_dict:
            attrition_dict[year] = [0] * 12

    # Prepare the chart data format
    return {
        "years": all_years,  # All years from 2008 to now
        "data": attrition_dict,
    }




def get_hiring_data():
    """
    Get hiring data grouped by year and month.
    """
    hiring_data = Profile.objects.filter(date_of_joining__isnull=False).annotate(
        year=ExtractYear('date_of_joining'),
        month=ExtractMonth('date_of_joining')
    ).values('year', 'month').annotate(count=Count('id')).order_by('year', 'month')

    # Generate a dictionary for hiring counts by year and month
    hiring_dict = defaultdict(lambda: [0] * 12)  # Default is a list of 12 zeros for each year
    for item in hiring_data:
        hiring_dict[item['year']][item['month'] - 1] = item['count']  # Zero-indexed months

    # Ensure years from 2008 to current year are included
    current_year = datetime.now().year
    all_years = list(range(2008, current_year + 1))
    for year in all_years:
        if year not in hiring_dict:
            hiring_dict[year] = [0] * 12

    # Prepare the chart data format
    return {
        "years": all_years,  # All years from 2008 to now
        "data": hiring_dict,
    }


def get_task_data(today):
    active_onboardings = Onboarding.objects.filter(entry_date__gte=today)
    past_due_tasks = OnboardingTasks.objects.filter(
        Q(state='ST') | Q(state='PR'), date_due__lt=today
    )[:10]
    tasks_due_week = OnboardingTasks.objects.filter(
        date_due__lt=today + timedelta(days=7), date_due__gte=today
    )[:10]
    return active_onboardings, past_due_tasks, tasks_due_week





@login_required
def main_page(request):
    if not request.user.is_staff:
        return main_page_user(request)

    today = timezone.now()
    applicant_profiles = Profile.objects.filter(applicant__isnull=False)

    # Get chart data
    gender_data = get_gender_data(applicant_profiles)
    age_data = get_age_data(applicant_profiles)
    attrition_data = get_attrition_data()
    hiring_data = get_hiring_data()

    # Get task data
    active_onboardings, past_due_tasks, tasks_due_week = get_task_data(today)

    # Context for rendering
    context = {
    'gender_data': json.dumps(gender_data),
    'age_data': json.dumps(age_data),
    'attrition_data': json.dumps(attrition_data),
    'attrition_years': attrition_data['years'],  # For dropdown
    'hiring_data': json.dumps(hiring_data),  # Hiring data for chart
    'hiring_years': hiring_data['years'],  # For dropdown
    # 'hiring_years' : [2020, 2021, 2022],  # Replace with your logic
    #  attrition_years = [2019, 2020, 2021]  # Replace with your logic
    'active_onboardings': active_onboardings,
    'past_due_tasks': past_due_tasks,
    'tasks_due_week': tasks_due_week,
    }
 
    return render(request, 'core/main.html', context)

def main_page_user(request):
    today = timezone.now()
    tasks_due = OnboardingTasks.objects.filter(
        Q(date_due__gte=today) | Q(date_due=None),
        assigned_to=request.user
    ).exclude(state=OnboardingTasks.COMPLETED)
    tasks_completed = OnboardingTasks.objects.filter(
        state=OnboardingTasks.COMPLETED, assigned_to=request.user
    ).order_by('-date_due')[:10]

    context = {
        'tasks_due': tasks_due,
        'tasks_completed': tasks_completed,
    }
    return render(request, 'core/main_user.html', context)
