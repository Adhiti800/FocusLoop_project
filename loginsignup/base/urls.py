from django.urls import path, include
from .views import (
    student_signup_view,
    welcome,
    teacher_info,
    student_info,
    teacher_signup_view,
)
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import path


app_name = 'base'

urlpatterns = [
    path("", welcome, name="welcome"),                     # Welcome page
    path("student_signup/", student_signup_view, name="student_signup"),
    path("signup_teach/", teacher_signup_view, name="teacher_signup"),
    path("teacher_info/", teacher_info, name="teacher_info"),
    path("student_info/", student_info, name="student_info"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path("accounts/", include("django.contrib.auth.urls")),  # Django auth URLs
   

]
