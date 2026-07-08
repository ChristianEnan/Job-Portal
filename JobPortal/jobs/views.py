from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render, get_object_or_404 ,  redirect
from django.contrib.auth.decorators import login_required

from applications.models import Application
from .models import Job


User = get_user_model()


def home(request):

    jobs = Job.objects.filter(is_active=True)

    search = request.GET.get("search")
    location = request.GET.get("location")
    job_type = request.GET.get("type")

    if search:
        jobs = jobs.filter(title__icontains=search)

    if location:
        jobs = jobs.filter(location__icontains=location)

    if job_type:
        jobs = jobs.filter(employment_type=job_type)

    context = {
        "jobs": jobs,
        "search": search,
        "location": location,
        "job_type": job_type,
        "employment_types": Job.EmploymentType.choices,
    }

    return render(request, "jobs/home.html", context)


@login_required

def apply_to_job(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    already = Application.objects.filter(
        candidate=request.user,
        job=job
    ).exists()

    if already:

        messages.warning(
            request,
            "You already applied for this job."
        )

        return redirect("job_detail", id=job.id)

    Application.objects.create(

        candidate=request.user,

        job=job

    )

    messages.success(
        request,
        "Application Submitted Successfully."
    )

    return redirect("job_detail", id=job.id)