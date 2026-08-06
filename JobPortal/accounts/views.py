from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect
from .models import CandidateProfile
from .forms import CandidateProfileForm
from jobs.models import Job, Company
from applications.models import Application, SavedJob, Interview


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

            if user.is_staff:
                return redirect("admin_dashboard")
            else:
                return redirect("dashboard")
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

    applied_jobs = Application.objects.filter(
        candidate=request.user
    ).count()

    saved_jobs = SavedJob.objects.filter(
        user=request.user
    ).count()

    interviews = Interview.objects.filter(
        application__candidate=request.user
    ).count()

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

    profile_completion = 0

    if request.user.username:
        profile_completion += 10

    if request.user.email:
        profile_completion += 10

    if profile.phone:
        profile_completion += 10

    if profile.city:
        profile_completion += 10

    if profile.skills:
        profile_completion += 15

    if profile.experience:
        profile_completion += 10

    if profile.resume:
        profile_completion += 15

    if profile.profile_image:
        profile_completion += 10

    if profile.github:
        profile_completion += 5

    if profile.linkedin:
        profile_completion += 5

    if profile.portfolio:
        profile_completion += 10

    return render(
        request,
        "accounts/profile.html",
        {
            "form": form,
            "profile": profile,
            "profile_completion": profile_completion,
            "applied_jobs": applied_jobs,
            "saved_jobs": 0,
            "interviews": interviews,
        }
    )


@login_required
def dashboard(request):

    applied_jobs = Application.objects.filter(
        candidate=request.user
    ).count()

    applications = Application.objects.filter(candidate=request.user).select_related("job")

    total_jobs = Job.objects.filter(
        is_active=True
    ).count()

    total_companies = Company.objects.count()

    recommended_jobs = Job.objects.filter(
    is_active=True
).select_related("company").order_by("-created_at")[:6]

    recent_activities = Application.objects.filter(
    candidate=request.user
).select_related(
    "job",
    "job__company"
).order_by("-applied_at")[:5]

    saved_jobs = SavedJob.objects.filter(user=request.user).count()

    profile = CandidateProfile.objects.filter(
        user=request.user
    ).first()

    profile_completion = 0

    if profile:

        if request.user.username:
            profile_completion += 10

        if request.user.email:
            profile_completion += 10

        if profile.phone:
            profile_completion += 10

        if profile.city:
            profile_completion += 10

        if profile.skills:
            profile_completion += 15

        if profile.experience:
            profile_completion += 10

        if profile.resume:
            profile_completion += 15

        if profile.profile_image:
            profile_completion += 10

        if profile.github:
            profile_completion += 5

        if profile.linkedin:
            profile_completion += 5

        if profile.portfolio:
            profile_completion += 10

    interviews = Interview.objects.filter(
    application__candidate=request.user
    ).select_related(
        "application",
        "application__job"
    ).order_by("interview_date", "interview_time")

    context = {
    "applied_jobs": applied_jobs,
    "total_jobs": total_jobs,
    "total_companies": total_companies,
    "saved_jobs": saved_jobs,
    "applications": applications,
    "interviews": interviews,
    "profile_completion":profile_completion,
    "recommended_jobs": recommended_jobs,
    "recent_activities": recent_activities,
}

    return render(
        request,
        "accounts/dashboard.html",
        context,
    )

@staff_member_required
def admin_dashboard(request):

    applications = Application.objects.select_related(
        "candidate",
        "job",
        "job__company"
    ).order_by("-applied_at")


    context = {
        "applications": applications,
    
    }

    return render(
        request,
        "accounts/admin_dashboard.html",
        context
    )

@staff_member_required
def update_application_status(request, pk):

    application = get_object_or_404(
        Application,
        pk=pk
    )

    if request.method == "POST":

        status = request.POST.get("status")

        if status in [
            "Pending",
            "Reviewed",
            "Shortlisted",
            "Rejected",
            "Selected"
        ]:
            application.status = status
            application.save()

    return redirect("admin_dashboard")