from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('home/', views.home, name='home'),  # optional separate name
    #path('teacher/', views.teacher_info, name='teacher_info'),
    #path('student/', views.student_info, name='student_info'),



]
