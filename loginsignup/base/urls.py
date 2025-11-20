
from django.urls import path, include
from .views import signup_view, home, welcome, teacher_info, student_info
from . import views


urlpatterns = [
  path("", views.welcome, name="welcome"),
  path("home/", home, name="home"),
  path("signup/", signup_view, name="signup_view"),
  path("teacher_info/", teacher_info, name = "teacher_info"),
  path("student_info/", student_info, name = "student_info"),
  path("accounts/", include("django.contrib.auth.urls")),
  path('login/', views.login_view, name='login'),
 # path("logout/", views.logout_view, name="logout"),
]
 