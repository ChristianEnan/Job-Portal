from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_POST

from .forms import ProfileCompletionForm
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
			"key_skills": profile.key_skills,
			"is_completed": profile.is_completed,
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
			key_skills=skills,
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


def profile_complete(request):
	if request.method == "POST":
		form = ProfileCompletionForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.cleaned_data
			user, _ = User.objects.get_or_create(
				username=data["username"],
				defaults={"email": data["email"]},
			)
			if not user.has_usable_password():
				user.set_unusable_password()
				user.save(update_fields=["password"])
			if user.email != data["email"]:
				user.email = data["email"]
				user.save(update_fields=["email"])

			profile, _ = CandidateProfile.objects.get_or_create(user=user)
			profile.profile_photo = data.get("profile_photo") or profile.profile_photo
			profile.phone = data.get("phone", "")
			profile.location = data.get("location", "")
			profile.education = data.get("education", "")
			profile.key_skills = data.get("key_skills", "")
			profile.languages = data.get("languages", "")
			profile.internships = data.get("internships", "")
			profile.projects = data.get("projects", "")
			profile.profile_summary = data.get("profile_summary", "")
			profile.accomplishments = data.get("accomplishments", "")
			profile.competitive_exams = data.get("competitive_exams", "")
			profile.employment = data.get("employment", "")
			profile.academic_achievements = data.get("academic_achievements", "")
			profile.resume = data.get("resume") or profile.resume
			profile.experience_years = data.get("experience_years") or 0
			profile.save()

			messages.success(request, "Profile completed successfully.")
			return redirect("profile-complete")
	else:
		form = ProfileCompletionForm()

	profiles = CandidateProfile.objects.select_related("user").all()[:6]
	return render(request, "accounts/profile_complete.html", {
		"form": form,
		"profiles": profiles,
	})
