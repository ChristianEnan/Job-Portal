from django.urls import path
from . import views

urlpatterns = [
    path(
        "my-applications/",
        views.my_applications,
        name="my_applications",
    ),
]