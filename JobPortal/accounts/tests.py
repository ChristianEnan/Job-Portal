from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import CandidateProfile


User = get_user_model()


class AccountsTests(TestCase):
	def test_create_profile_endpoint(self):
		response = self.client.post(
			reverse("profile-create"),
			{
				"username": "alice",
				"email": "alice@example.com",
				"password": "StrongPass123",
				"phone": "1234567890",
				"location": "Mumbai",
				"skills": "Python,Django",
			},
		)

		self.assertEqual(response.status_code, 201)
		self.assertTrue(User.objects.filter(username="alice").exists())
		self.assertTrue(CandidateProfile.objects.filter(user__username="alice").exists())

	def test_profile_list_endpoint(self):
		user = User.objects.create_user(username="john", email="john@example.com", password="abc123")
		CandidateProfile.objects.create(user=user, phone="999", location="Delhi", skills="Django")

		response = self.client.get(reverse("profile-list"))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "john")
