from django.contrib import admin
from .models import CandidateProfile


@admin.register(CandidateProfile)
class CandidateProfileAdmin(admin.ModelAdmin):
	list_display = ("user", "location", "experience_years", "is_completed", "created_at")
	search_fields = (
		"user__username",
		"user__email",
		"phone",
		"location",
		"education",
		"key_skills",
	)
	list_filter = ("is_completed", "location", "experience_years")
