from django.contrib import admin
from .models import Application, SavedJob, Interview

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "candidate",
        "job",
        "status",
        "applied_at",
    )

    list_editable = ("status",)

    @admin.register(Interview)
    class InterviewAdmin(admin.ModelAdmin):

       list_display = (
        "application",
        "interview_date",
        "interview_time",
    )

       search_fields = (
        "application__candidate__username",
        "application__job__title",
    )