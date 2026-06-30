from django.db import models
from jobs.models import Job

class Application(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name

