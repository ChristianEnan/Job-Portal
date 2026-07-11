from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CandidateProfile
from .forms import CandidateProfileForm
from jobs.models import Job, Company
from applications.models import Application

def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("home")

    else:

        form = UserCreationForm()

    return render(request, "accounts/register.html", {
        "form": form
    })


def user_login(request):

    error = ""

    if request.method == "POST":

        username = request.POST["username"]

        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return redirect("home")

        else:

            error = "Invalid Username or Password"

    return render(request,
                  "accounts/login.html",
                  {
                      "error": error
                  })


def user_logout(request):

    logout(request)

    return redirect("home")

    
@login_required
    
def profile(request):

    profile, created = CandidateProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        form = CandidateProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():

            form.save()

            return redirect("profile")

    else:

        form = CandidateProfileForm(instance=profile)

    return render(
        request,
        "accounts/profile.html",
        {
            "form": form,
            "profile": profile
        }
    )

    logout(request)

    return redirect("home")

@login_required
def dashboard(request):

    applied_jobs = Application.objects.filter(
        candidate=request.user
    ).count()

    total_jobs = Job.objects.filter(
        is_active=True
    ).count()

    total_companies = Company.objects.count()

    context = {
        "applied_jobs": applied_jobs,
        "total_jobs": total_jobs,
        "total_companies": total_companies,
        "saved_jobs": 0,
    }

    return render(
        request,
        "accounts/dashboard.html",
        context,
    )