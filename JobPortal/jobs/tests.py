from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Job
from applications.models import Application


User = get_user_model()


class JobsTests(TestCase):
	def setUp(self):
		self.job = Job.objects.create(
			title="Backend Developer",
			company="Acme",
			location="Remote",
			salary="10 LPA",
			description="Build backend APIs",
		)
		self.user = User.objects.create_user(
			username="candidate1",
			email="candidate1@example.com",
			password="StrongPass123",
		)

	def test_home_page_loads(self):
		response = self.client.get(reverse("home"))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Backend Developer")

	def test_job_detail_page_loads(self):
		response = self.client.get(reverse("job-detail", kwargs={"job_id": self.job.id}))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Acme")

	def test_home_filter_by_query(self):
		Job.objects.create(
			title="UI Designer",
			company="Design Co",
			location="Remote",
			salary="7 LPA",
			description="Design interfaces",
		)
		response = self.client.get(reverse("home"), {"q": "Backend"})
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Backend Developer")
		self.assertNotContains(response, "UI Designer")

	def test_apply_to_job_creates_application(self):
		response = self.client.post(
			reverse("job-apply", kwargs={"job_id": self.job.id}),
			{
				"username": "candidate1",
				"cover_letter": "I match this role well.",
			},
			follow=True,
		)
		self.assertEqual(response.status_code, 200)
		self.assertTrue(Application.objects.filter(job=self.job, candidate=self.user).exists())
