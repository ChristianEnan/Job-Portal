from django.urls import path
from .views import apply_to_job, home, job_detail

urlpatterns = [
    path('', home, name='home'),
    path('jobs/<int:job_id>/', job_detail, name='job-detail'),
    path('jobs/<int:job_id>/apply/', apply_to_job, name='job-apply'),
]