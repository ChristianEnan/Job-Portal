from django.urls import path
from . import views

urlpatterns = [
    path(
        "my-applications/",
        views.my_applications,
        name="my_applications",
    ),

     path(
        "save/<int:job_id>/",
        views.save_job,
        name="save_job"
    ),

     path(
       "saved/",
       views.saved_jobs,
       name="saved_jobs"
    ),

     path(
       "unsave/<int:job_id>/",
       views.unsave_job,
       name="unsave_job",
    ),

    path(
        "schedule-interview/<int:application_id>/",
        views.schedule_interview,
        name="schedule_interview",
    ),

    path(
        "applicants/",
        views.applicants,
        name="applicants",
    ),
]
