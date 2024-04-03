from django.urls import path

from .views import RegistrationUserView

urlpatterns = [
    path("api/signup/", RegistrationUserView.as_view(), name="signup"),
]
