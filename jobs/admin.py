from django.contrib import admin
from .models import Job, Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "website",
        "email"
    )


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "company",
        "location",
        "employment_type",
        "is_active"
    )

    search_fields = (
        "title",
        "company__name"
    )

    list_filter = (
        "employment_type",
        "is_active"
    )