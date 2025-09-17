from django.urls import path
from . import views

urlpatterns = [
    path('', views.employer_dashboard, name='employer'),  # Employer Dashboard
    path('profile/', views.employer_profile, name='employer_profile'),
     path('edit-job/<int:job_id>/', views.edit_job, name='edit_job'),
    path('delete-job/<int:job_id>/', views.delete_job, name='delete_job'),
    path('manage-job/', views.manage_job, name='manage_job'),
    path('post-new-job/', views.post_new_job, name='post_new_job'),
    path('view-applicants/', views.view_applicants, name='view_applicants'),
]
