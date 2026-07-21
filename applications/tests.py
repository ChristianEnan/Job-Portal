from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from jobs.models import Job
from .models import Application


User = get_user_model()


class ApplicationsTests(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username="bob", email="bob@example.com", password="abc123")
		self.job = Job.objects.create(
			title="QA Engineer",
			company="Acme",
			location="Pune",
			salary="8 LPA",
			description="Test web apps",
		)

	def test_apply_for_job_endpoint(self):
		response = self.client.post(
			reverse("application-create"),
			{
				"username": "bob",
				"job_id": self.job.id,
				"cover_letter": "I am a good fit",
			},
		)
		self.assertEqual(response.status_code, 201)
		self.assertTrue(Application.objects.filter(job=self.job, candidate=self.user).exists())

	def test_application_list_endpoint(self):
		Application.objects.create(job=self.job, candidate=self.user, cover_letter="Test")
		response = self.client.get(reverse("application-list"))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "QA Engineer")
