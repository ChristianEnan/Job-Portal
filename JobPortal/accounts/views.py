from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST

from .models import CandidateProfile


User = get_user_model()


@require_GET
def profile_list(request):
	profiles = CandidateProfile.objects.select_related("user").all()
	data = [
		{
			"id": profile.id,
			"username": profile.user.get_username(),
			"email": profile.user.email,
			"phone": profile.phone,
			"location": profile.location,
			"experience_years": profile.experience_years,
		}
		for profile in profiles
	]
	return JsonResponse({"profiles": data})


@require_POST
def create_profile(request):
	username = request.POST.get("username", "").strip()
	email = request.POST.get("email", "").strip()
	password = request.POST.get("password", "").strip()
	phone = request.POST.get("phone", "").strip()
	location = request.POST.get("location", "").strip()
	skills = request.POST.get("skills", "").strip()

	if not username or not email or not password:
		return JsonResponse({"error": "username, email, and password are required"}, status=400)

	try:
		user = User.objects.create_user(username=username, email=email, password=password)
		profile = CandidateProfile.objects.create(
			user=user,
			phone=phone,
			location=location,
			skills=skills,
		)
	except IntegrityError:
		return JsonResponse({"error": "user already exists"}, status=400)

	return JsonResponse(
		{
			"id": profile.id,
			"username": user.get_username(),
			"email": user.email,
		},
		status=201,
	)
