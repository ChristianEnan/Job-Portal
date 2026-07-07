from django.db import models
from django.contrib.auth.models import User
from jobs.models import Job


class Application(models.Model):

    candidate = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )

    cover_letter = models.TextField(blank=True)

    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("candidate", "job")

    def __str__(self):
        return f"{self.candidate.username} - {self.job.title}"