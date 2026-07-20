from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render, get_object_or_404 ,  redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from applications.models import Application
from .models import Job
from .models import Job, Company
from .forms import CompanyForm, JobForm
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

def job_detail(request, id):
    job = get_object_or_404(Job, id=id)

    return render(
        request,
        "jobs/detail.html",
        {
            "job": job
        }
    )

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

def company_detail(request, id):

    company = get_object_or_404(Company, id=id)

    jobs = Job.objects.filter(
        company=company,
        is_active=True
    )

    context = {
        "company": company,
        "jobs": jobs,
    }

    return render(
        request,
        "jobs/company_detail.html",
        context,
    )

@staff_member_required
def company_list(request):

    companies = Company.objects.all().order_by("name")

    return render(
        request,
        "jobs/company_list.html",
        {
            "companies": companies
        }
    )

@staff_member_required
def add_company(request):

    if request.method == "POST":

        form = CompanyForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect("company_list")

    else:

        form = CompanyForm()

    return render(
        request,
        "jobs/add_company.html",
        {
            "form": form
        }
    )

@staff_member_required
def edit_company(request, pk):

    company = get_object_or_404(
        Company,
        pk=pk
    )

    if request.method == "POST":

        form = CompanyForm(
            request.POST,
            request.FILES,
            instance=company
        )

        if form.is_valid():

            form.save()

            return redirect("company_list")

    else:

        form = CompanyForm(instance=company)

    return render(
        request,
        "jobs/edit_company.html",
        {
            "form": form,
            "company": company
        }
    )

@staff_member_required
def delete_company(request, pk):

    company = get_object_or_404(
        Company,
        pk=pk
    )

    if request.method == "POST":

        company.delete()

        return redirect("company_list")

    return render(
        request,
        "jobs/delete_company.html",
        {
            "company": company
        }
    )

@staff_member_required
def add_job(request):

    if request.method == "POST":

        form = JobForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect("home")

    else:

        form = JobForm()

    return render(
        request,
        "jobs/add_job.html",
        {
            "form": form
        }
    )

@staff_member_required
def manage_jobs(request):

    jobs = Job.objects.select_related(
        "company"
    ).order_by("-id")

    return render(
        request,
        "jobs/manage_jobs.html",
        {
            "jobs": jobs
        }
    )

from django.shortcuts import get_object_or_404

@staff_member_required
def edit_job(request, pk):

    job = get_object_or_404(Job, pk=pk)

    if request.method == "POST":

        form = JobForm(request.POST, instance=job)

        if form.is_valid():

            form.save()

            return redirect("manage_jobs")

    else:

        form = JobForm(instance=job)

    return render(
        request,
        "jobs/edit_job.html",
        {
            "form": form,
            "job": job
        }
    )

@staff_member_required
def delete_job(request, pk):

    job = get_object_or_404(Job, pk=pk)

    if request.method == "POST":

        job.delete()

        return redirect("manage_jobs")

    return render(
        request,
        "jobs/delete_job.html",
        {
            "job": job
        }
    )