from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


User = get_user_model()


class CandidateProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="candidate_profile")
	profile_photo = models.FileField(upload_to="profile_photos/", blank=True, default="")
	phone = models.CharField(max_length=20, blank=True, default="")
	location = models.CharField(max_length=120, blank=True, default="")
	education = models.TextField(blank=True, default="")
	key_skills = models.TextField(blank=True, default="")
	languages = models.TextField(blank=True, default="")
	internships = models.TextField(blank=True, default="")
	projects = models.TextField(blank=True, default="")
	profile_summary = models.TextField(blank=True, default="")
	accomplishments = models.TextField(blank=True, default="")
	competitive_exams = models.TextField(blank=True, default="")
	employment = models.TextField(blank=True, default="")
	academic_achievements = models.TextField(blank=True, default="")
	resume = models.FileField(upload_to="resumes/", blank=True, default="")
	experience_years = models.PositiveIntegerField(default=0)
	is_completed = models.BooleanField(default=False)
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ["-created_at"]

	def __str__(self):
		return f"{self.user.get_username()} profile"

	def save(self, *args, **kwargs):
		self.is_completed = any([
			self.profile_photo,
			self.education,
			self.key_skills,
			self.languages,
			self.internships,
			self.projects,
			self.profile_summary,
			self.accomplishments,
			self.competitive_exams,
			self.employment,
			self.academic_achievements,
			self.resume,
		])
		self.updated_at = timezone.now()
		super().save(*args, **kwargs)
