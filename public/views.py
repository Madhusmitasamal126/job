from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Job, Category, Company, Testimonial

from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render
from .models import Job

def home(request):
    jobs = Job.objects.all()
    query = request.GET.get('q')
    location = request.GET.get('location')

    if query:
        jobs = jobs.filter(title__icontains=query)  # Search in job title
    if location:
        jobs = jobs.filter(location__icontains=location)  # Search in location

    categories = Category.objects.all()  # If you have categories
    companies = Company.objects.all()  # For carousel
    testimonials = Testimonial.objects.all()
    job_types = ['Full-time', 'Part-time', 'Internship']  # or fetch dynamically
    locations = Job.objects.values_list('location', flat=True).distinct()

    context = {
        'jobs': jobs,
        'categories': categories,
        'companies': companies,
        'testimonials': testimonials,
        'job_types': job_types,
        'locations': locations,
    }
    return render(request, 'public/index.html', context)


def about(request):
    return render(request, "public/about.html", {"year": datetime.now().year})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        # TODO: Save to DB or send email
        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")
    return render(request, "public/contact.html", {"year": datetime.now().year})

# Register
def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Registration successful. Please login.')
        return redirect('login')

    return render(request, 'public/registration.html')
# Login
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')

    return render(request, 'public/login.html')

def logout_user(request):
    logout(request)
    return redirect("login")

def job_list(request):
    jobs = Job.objects.all().order_by('-posted_on')
    return render(request, 'public/job_listing.html', {'jobs': jobs})

# Job Details
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'public/job_details.html', {'job': job})
