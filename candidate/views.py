from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CandidateProfile, JobApplication
from public.models import Job
from .forms import CandidateProfileForm, JobApplicationForm

@login_required
def candidate_dashboard(request):
    return render(request, 'candidate/candidate.html')

@login_required
def browse_jobs(request):
    query = request.GET.get('q')
    jobs = Job.objects.all()
    if query:
        jobs = jobs.filter(title__icontains=query)
    return render(request, 'candidate/browse_jobs.html', {'jobs': jobs})

@login_required
def job_application(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job = job
            application.save()
            return redirect('applied_jobs')
    else:
        form = JobApplicationForm()
    return render(request, 'candidate/apply_job.html', {'form': form, 'job': job})

@login_required
def applied_jobs(request):
    applications = JobApplication.objects.filter(user=request.user)
    return render(request, 'candidate/applied_jobs.html', {'applications': applications})

@login_required
def profile_management(request):
    profile, created = CandidateProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = CandidateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('candidate_dashboard')
    else:
        form = CandidateProfileForm(instance=profile)
    return render(request, 'candidate/profile_management.html', {'form': form, 'profile': profile})
