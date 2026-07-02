from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render, get_object_or_404 ,  redirect
from django.views.decorators.http import require_POST

from applications.models import Application
from .models import Job


User = get_user_model()


def home(request):
    jobs = Job.objects.all()

    return render(request, 'jobs/home.html', {
        'jobs': jobs
    })


def job_detail(request, id):
    job = get_object_or_404(Job, id=id)

    return render(request, 'jobs/detail.html', {
        'job': job
    })


@require_POST
def apply_to_job(request, job_id):
    try:
        job = Job.objects.get(pk=job_id, is_active=True)
    except Job.DoesNotExist as exc:
        raise Http404("Job not found") from exc

    username = request.POST.get("username", "").strip()
    cover_letter = request.POST.get("cover_letter", "").strip()

    if not username:
        messages.error(request, "Username is required to apply.")
        return redirect("job-detail", id=job.id)

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        messages.error(
            request,
            "Candidate account not found. Create one first in /accounts/create/.",
        )
        return redirect("job-detail", id=job.id)

    application, created = Application.objects.get_or_create(
        job=job,
        candidate=user,
        defaults={"cover_letter": cover_letter},
    )

    if created:
        messages.success(request, f"Application submitted for {job.title}.")
    else:
        messages.info(request, f"You already applied for {job.title}.")

    return redirect("job-detail", id=job.id)


