from django.shortcuts import render
from django.http import Http404

from .models import Job


def home(request):
    jobs = Job.objects.filter(is_active=True)

    return render(request, 'jobs/home.html', {
        'jobs': jobs
    })


def job_detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id, is_active=True)
    except Job.DoesNotExist as exc:
        raise Http404("Job not found") from exc

    return render(request, 'jobs/detail.html', {
        'job': job
    })


