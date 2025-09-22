from django.urls import path
from . import views

urlpatterns = [
    path('', views.employer_dashboard, name='employer_dashboard'),
    path('profile/', views.profile_view, name='employer_profile'),  # <- Add this
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('jobs/manage/', views.manage_job, name='manage_job'),
    path('jobs/post/', views.post_new_job, name='post_new_job'),
    path('jobs/edit/<int:job_id>/', views.edit_job, name='edit_job'),
    path('jobs/delete/<int:job_id>/', views.delete_job, name='delete_job'),
    path('applicants/', views.view_applicants, name='view_applicants'),
    path('jobs/apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('profile/', views.profile_view, name='profile_view'), 
    path('jobs/confirm/<int:job_id>/', views.confirm_application, name='confirm_application'),
]
