
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from base.models import Teacher, Student

@login_required
def home(request):
    user = request.user
    teacher = None
    student = None
    if hasattr(user, 'teacher'):
        teacher = user.teacher
    if hasattr(user, 'student'):
        student = user.student

    context = {
        'user': user,
        'teacher': teacher,
        'student': student,
    }
    return render(request, 'home.html', context)

# views.py example
from django.shortcuts import render
from .models import LeaveRecord

def teacher_dashboard(request):
    # Fetch all leave records that haven't been approved yet, ordered by when they were sent
    pending_leaves = LeaveRecord.objects.filter(is_approved=False).order_by('-sent_on')

    context = {
        'pending_leaves': pending_leaves
    }
    return render(request, 'dashboard.html', context)

