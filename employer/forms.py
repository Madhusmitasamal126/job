from django import forms
from .models import EmployerProfile, Job

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = ["company_name", "industry", "location", "website", "about"]


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["title", "location", "salary", "description"]

# from django import forms
# from .models import Job

# class JobForm(forms.ModelForm):
#     class Meta:
#         model = Job
#         fields = ['title', 'description', 'location', 'salary', 'status']
#         widgets = {
#             'description': forms.Textarea(attrs={'rows': 4}),
#         }
