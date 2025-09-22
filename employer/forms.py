from django import forms
from .models import EmployerProfile, Job, Application, UserProfile

# Employer Profile Form
class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = ['company_name', 'website', 'industry', 'phone', 'address', 'description', 'resume', 'avatar']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

# Job Form
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["title", "location", "salary", "description"]

# Application Form
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["name", "email", "resume", "cover_letter"]

# # Candidate Profile Form
# from django import forms
# from .models import UserProfile, EmployerProfile
class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'phone', 'dob', 'address', 'education', 'experience', 'skills', 'resume']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'experience': forms.Textarea(attrs={'rows': 3}),
            'skills': forms.Textarea(attrs={'rows': 2}),
            'address': forms.Textarea(attrs={'rows': 2}),
        }
# Employer Form
# class EmployerProfileForm(forms.ModelForm):
#     class Meta:
#         model = EmployerProfile
#         fields = ['avatar', 'company_name', 'website', 'industry', 'phone', 'address', 'description', 'resume']


class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'phone', 'dob', 'address', 'education', 'experience', 'skills', 'resume']

# class EmployerProfileForm(forms.ModelForm):
#     class Meta:
#         model = EmployerProfile
#         fields = ['avatar', 'company_name', 'website', 'industry', 'phone', 'address', 'description', 'resume']
