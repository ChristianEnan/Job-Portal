from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('job/<int:id>/', views.job_detail, name='job_detail'),
    path("apply/<int:job_id>/", views.apply_to_job, name="apply_job",),
    path("company/<int:id>/", views.company_detail, name="company_detail"),
]