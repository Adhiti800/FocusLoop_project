from django.urls import path, include
from .views import (
    student_signup_view,
    welcome,
    teacher_info,
    student_info,
    login_view,
    logout_view,
    teacher_signup_view,
)

app_name = 'base'

urlpatterns = [
    path("", welcome, name="welcome"),                     # Welcome page
    path("student_signup/", student_signup_view, name="student_signup"),
    path("signup_teach/", teacher_signup_view, name="teacher_signup"),
    path("teacher_info/", teacher_info, name="teacher_info"),
    path("student_info/", student_info, name="student_info"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("accounts/", include("django.contrib.auth.urls")),  # Django auth URLs
]
