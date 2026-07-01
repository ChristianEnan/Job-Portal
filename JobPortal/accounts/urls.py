from django.urls import path

from .views import create_profile, profile_list

urlpatterns = [
    path("", profile_list, name="profile-list"),
    path("create/", create_profile, name="profile-create"),
]
