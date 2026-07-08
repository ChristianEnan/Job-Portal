from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Application


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