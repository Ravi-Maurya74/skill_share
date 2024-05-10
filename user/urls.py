from django.urls import path
from user import views

urlpatterns = [path("", views.AuthenticateUser.as_view(), name="authenticate_user")]
