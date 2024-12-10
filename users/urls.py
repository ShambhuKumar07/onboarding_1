from django.urls import path
from .views import login_view,logout_view,profile_detail_view
from . import views
app_name = 'users'

urlpatterns = [
    path('login/',login_view,name='login_view'),
    path('logout/',logout_view,name='logout_view'),
    path('profile/<int:profile_id>/', profile_detail_view, name='profile_detail'),
    path('attrition-report/', views.attrition_report, name='attrition_report'),
    path('hiring-report/', views.hiring_report, name='hiring_report'),
    path('users/export-all/', views.export_applicants_to_excel, name='export_mis_report'),
]
