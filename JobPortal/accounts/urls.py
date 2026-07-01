from django.urls import path

from .views import create_profile, profile_complete, profile_list

urlpatterns = [
    path("", profile_list, name="profile-list"),
    path("create/", create_profile, name="profile-create"),
    path("complete/", profile_complete, name="profile-complete"),
]
