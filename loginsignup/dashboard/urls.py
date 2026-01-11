from django.urls import path
from . import views


app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_router, name='home'),               # unified router
    path('student/', views.student_home_view, name='student_home'),
    path('teacher/', views.teacher_home_view, name='teacher_home'),
    path('student_complain/', views.student_complain_view, name='student_complain'),
    path('update_complaint/<int:complaint_id>/', views.update_complaint_status, name='update_complaint'),
    path('student_leave/', views.student_leave_view, name='student_leave'),
    path('teacher_leave_requests/', views.teacher_leave_view, name='teacher_leave_requests'),

]

