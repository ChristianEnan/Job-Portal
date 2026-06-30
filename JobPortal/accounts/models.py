from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class CandidateProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="candidate_profile")
	phone = models.CharField(max_length=20)
	location = models.CharField(max_length=120)
	skills = models.TextField(help_text="Comma-separated skills")
	resume = models.TextField(blank=True)
	experience_years = models.PositiveIntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self):
		return f"{self.user.get_username()} profile"
