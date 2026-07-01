from django.test import TestCase
from django.urls import reverse

from .models import Job


class JobsTests(TestCase):
	def setUp(self):
		self.job = Job.objects.create(
			title="Backend Developer",
			company="Acme",
			location="Remote",
			salary="10 LPA",
			description="Build backend APIs",
		)

	def test_home_page_loads(self):
		response = self.client.get(reverse("home"))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Backend Developer")

	def test_job_detail_page_loads(self):
		response = self.client.get(reverse("job-detail", kwargs={"job_id": self.job.id}))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Acme")
