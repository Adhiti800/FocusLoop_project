from django.urls import path
from . import views


app_name = 'dashboard'

urlpatterns = [
    path('home/', views.dashboard_router, name='home'),               # unified router
    path('dashboard/student_home/', views.student_home_view, name='student_home'),
    path('dashboard/teacher_home/', views.teacher_home_view, name='teacher_home'),
    path('student_complain/', views.student_complain_view, name='student_complain'),
    path('update_complaint/<int:complaint_id>/', views.update_complaint_status, name='update_complaint'),
    path('dashboard/student_leave/', views.student_leave_view, name='student_leave'),
    path('teacher_leave_requests/', views.teacher_leave_view, name='teacher_leave_requests'),

]

