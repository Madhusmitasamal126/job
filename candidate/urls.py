from django.urls import path
from . import views

urlpatterns = [
    path('', views.candidate_dashboard, name='candidate_dashboard'),
    path('browse_jobs/', views.browse_jobs, name='browse_jobs'),
    path('applied_jobs/', views.applied_jobs, name='applied_jobs'),
    path('apply/<int:job_id>/', views.job_application, name='job_application'),
    path('profile/', views.profile_management, name='profile_management'),
]
