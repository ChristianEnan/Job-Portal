from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

from .models import Application, Interview
from jobs.models import Job
from .models import SavedJob


@login_required
def my_applications(request):

    applications = Application.objects.filter(
        candidate=request.user
    ).select_related("job")

    return render(
        request,
        "applications/my_applications.html",
        {
            "applications": applications
        }
    )

@login_required
def save_job(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    saved, created = SavedJob.objects.get_or_create(
        user=request.user,
        job=job
    )

    if created:
        messages.success(request, "Job saved successfully.")
    else:
        messages.warning(request, "Job already saved.")

    return redirect("job_detail", id=job.id)

@login_required
def saved_jobs(request):

    saved_jobs = SavedJob.objects.filter(
        user=request.user
    ).select_related("job", "job__company")

    context = {
        "saved_jobs": saved_jobs
    }

    return render(
        request,
        "applications/saved_jobs.html",
        context
    )

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import SavedJob


@login_required
def unsave_job(request, job_id):

    saved = SavedJob.objects.filter(
        user=request.user,
        job_id=job_id
    )

    if saved.exists():
        saved.delete()

    return redirect("saved_jobs")

def schedule_interview(request, application_id):

    application = get_object_or_404(
        Application,
        id=application_id
    )

    if request.method == "POST":

        interview_date = request.POST.get("interview_date")
        interview_time = request.POST.get("interview_time")
        meeting_link = request.POST.get("meeting_link")
        location = request.POST.get("location")
        notes = request.POST.get("notes")

        Interview.objects.update_or_create(
            application=application,
            defaults={
                "interview_date": interview_date,
                "interview_time": interview_time,
                "meeting_link": meeting_link,
                "location": location,
                "notes": notes,
            }
        )

        application.status = "Shortlisted"
        application.save()

        return redirect("admin_dashboard")

    return render(
        request,
        "applications/schedule_interview.html",
        {
            "application": application
        }
    )

@staff_member_required
def applicants(request):

    applications = Application.objects.select_related(
        "candidate",
        "job"
    ).all()

    context = {
        "applications": applications
    }

    return render(
        request,
        "applications/applicants.html",
        context
    )