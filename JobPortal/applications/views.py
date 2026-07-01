from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST

from jobs.models import Job
from .models import Application


User = get_user_model()


@require_GET
def application_list(request):
	applications = Application.objects.select_related("job", "candidate").all()
	data = [
		{
			"id": app.id,
			"job": app.job.title,
			"candidate": app.candidate.get_username(),
			"status": app.status,
			"created_at": app.created_at.isoformat(),
		}
		for app in applications
	]
	return JsonResponse({"applications": data})


@require_POST
def apply_for_job(request):
	username = request.POST.get("username", "").strip()
	job_id = request.POST.get("job_id", "").strip()
	cover_letter = request.POST.get("cover_letter", "").strip()

	if not username or not job_id:
		return JsonResponse({"error": "username and job_id are required"}, status=400)

	try:
		user = User.objects.get(username=username)
	except User.DoesNotExist:
		return JsonResponse({"error": "candidate does not exist"}, status=404)

	try:
		job = Job.objects.get(pk=job_id, is_active=True)
	except Job.DoesNotExist:
		return JsonResponse({"error": "job not found"}, status=404)

	application, created = Application.objects.get_or_create(
		job=job,
		candidate=user,
		defaults={"cover_letter": cover_letter},
	)

	if not created:
		return JsonResponse({"error": "application already exists"}, status=400)

	return JsonResponse(
		{
			"id": application.id,
			"job": application.job.title,
			"candidate": application.candidate.get_username(),
			"status": application.status,
		},
		status=201,
	)
