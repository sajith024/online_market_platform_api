from django.urls import path

from .views import RegistrationUserView, RolesView, RoleDetailsView

urlpatterns = [
    path("api/signup/", RegistrationUserView.as_view(), name="signup"),
    path("api/roles/", RolesView.as_view(), name="roles"),
    path("api/role/<int:pk>", RoleDetailsView.as_view(), name="role_details"),
]
