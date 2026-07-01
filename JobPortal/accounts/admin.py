from django.contrib import admin
from .models import CandidateProfile


@admin.register(CandidateProfile)
class CandidateProfileAdmin(admin.ModelAdmin):
	list_display = ("user", "phone", "location", "experience_years", "created_at")
	search_fields = ("user__username", "user__email", "phone", "location")
	list_filter = ("location", "experience_years")
