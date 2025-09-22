from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import EmployerProfile, Job, Applicant
from .forms import EmployerProfileForm, JobForm, ApplicationForm, CandidateProfileForm

@login_required
def employer_dashboard(request):
    return render(request, "employers/employer.html")

@login_required
def profile_view(request):
    user = request.user
    if hasattr(user, "employerprofile"):
        profile = user.employerprofile
        user_type = "employer"
    else:
        profile = user.userprofile
        user_type = "candidate"

    skills_list = []
    if user_type == "candidate" and profile.skills:
        skills_list = [s.strip() for s in profile.skills.split(",")]

    return render(request, "employers/employer_profile.html", {
        "profile": profile,
        "user_type": user_type,
        "skills_list": skills_list
    })
@login_required
def profile_edit(request):
    user = request.user
    profile = getattr(user, 'employerprofile', None)

    if request.method == 'POST':
        form = EmployerProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            # Redirect to profile view page after saving
            return redirect('profile_view')
    else:
        form = EmployerProfileForm(instance=profile)

    return render(request, 'employers/profile_edit.html', {'form': form})


@login_required
def manage_job(request):
    jobs = Job.objects.filter(employer__user=request.user)
    return render(request, "employers/manage_job.html", {"jobs": jobs})

@login_required
def post_new_job(request):
    profile = EmployerProfile.objects.get(user=request.user)
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = profile
            job.save()
            return redirect("manage_job")
    else:
        form = JobForm()
    return render(request, "employers/post_new_job.html", {"form": form})

@login_required
def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, employer__user=request.user)
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('manage_job')
    else:
        form = JobForm(instance=job)
    return render(request, "employers/edit_job.html", {"form": form, "job": job})

@login_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, employer__user=request.user)
    if request.method == "POST":
        job.delete()
        return redirect('manage_job')
    return render(request, "employers/delete_job.html", {"job": job})

@login_required
def view_applicants(request):
    jobs = Job.objects.filter(employer__user=request.user)
    applicants = Applicant.objects.filter(job__in=jobs)
    return render(request, "employers/view_applicants.html", {"applicants": applicants})

@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return redirect("job_detail", job.id)
    else:
        form = ApplicationForm()
    return render(request, "apply_job.html", {"form": form, "job": job})

@login_required
def confirm_application(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, "confirm_application.html", {"job": job})
