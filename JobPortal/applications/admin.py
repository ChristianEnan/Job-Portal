from django.contrib import admin
from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
	list_display = ("job", "candidate", "status", "created_at")
	search_fields = ("job__title", "candidate__username", "candidate__email")
	list_filter = ("status", "created_at")
