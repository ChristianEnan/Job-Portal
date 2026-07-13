from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from .models import Application
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