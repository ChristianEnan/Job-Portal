from django.db import models
from django.contrib.auth import get_user_model

from jobs.models import Job


User = get_user_model()


class Application(models.Model):
    class Status(models.TextChoices):
        APPLIED = "applied", "Applied"
        REVIEWING = "reviewing", "Reviewing"
        SHORTLISTED = "shortlisted", "Shortlisted"
        REJECTED = "rejected", "Rejected"
        HIRED = "hired", "Hired"

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    candidate = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
    cover_letter = models.TextField(blank=True)
    resume = models.FileField(upload_to="resumes/", blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.APPLIED)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ("job", "candidate")

    def __str__(self):
        return f"{self.candidate.get_username()} -> {self.job.title}"

