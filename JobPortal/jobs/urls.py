from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('job/<int:id>/', views.job_detail, name='job_detail'),
    path("apply/<int:job_id>/", views.apply_to_job, name="apply_job",),
    path("company/<int:id>/", views.company_detail, name="company_detail"),
    path("companies/",views.company_list,name="company_list",),
    path("companies/add/",views.add_company,name="add_company",),
    path("companies/edit/<int:pk>/",views.edit_company,name="edit_company",),
    path("companies/delete/<int:pk>/",views.delete_company,name="delete_company",),
    path("jobs/add/",views.add_job,name="add_job",),
]