from django.urls import path

from .views import application_list, apply_for_job

urlpatterns = [
    path("", application_list, name="application-list"),
    path("apply/", apply_for_job, name="application-create"),
]
