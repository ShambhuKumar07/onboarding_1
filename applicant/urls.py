# applicant/urls.py
from django.urls import path
from .views1 import applicant_dashboard
from applicant import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'applicant'

urlpatterns = [
    path('dashboard/', applicant_dashboard, name='dashboard'),
    path('page_1/', views.page_1, name='page_1'),
    path('page/2/', views.page_2, name='page_2'),
    # path('save_page_2/', views.page_2, name='save_page_2'), 
    path('page/3/', views.page_3, name='page_3'),
    path('page/4/', views.page_4, name='page_4'),
    path('page/5/', views.page_5, name='page_5'),
    path('page/6/', views.page_6, name='page_6'),
    path('page/7/', views.page_7, name='page_7'),
    path('languages_known/', views.languages_known, name='languages_known'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)