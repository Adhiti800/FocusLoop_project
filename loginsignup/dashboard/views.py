from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Complaint, LeaveRecord


# ------------------------------
# Dashboard router: redirect based on role
# ------------------------------

def dashboard_router(request):
    user = request.user

    if hasattr(user, 'teacher'):
        return redirect('dashboard:teacher_home')

    if hasattr(user, 'student'):
        return redirect('dashboard:student_home')

    return redirect('base:welcome')


# ------------------------------
# Student home/dashboard
# ------------------------------

def student_home_view(request):
    student = request.user.student
    leave_count = LeaveRecord.objects.filter(student=student).count()
    complaint_count = Complaint.objects.filter(student=student).count()

    return render(request, 'dashboard/student_home.html', {
        "student": student,
        "leave_count": leave_count,
        "complaint_count": complaint_count,
    })



# ------------------------------
# Teacher home/dashboard
# ------------------------------

def teacher_home_view(request):
    teacher = request.user.teacher
    leave_count = LeaveRecord.objects.filter(student__student_class=teacher.class_assigned).count()
    complaint_count = Complaint.objects.all().count()  # Or filter by class/section

    return render(request, "dashboard/teacher_home.html", {
        "teacher": teacher,
        "leave_count": leave_count,
        "complaint_count": complaint_count,
    })

# ------------------------------
# Student complaints
# ------------------------------

def student_complain_view(request):
    student = request.user.student

    if request.method == 'POST':
        complaint_title = request.POST.get('complaint_title')
        complaint_category = request.POST.get('complaint_category')
        complaint_detail = request.POST.get('complaint_detail')
        anonymous = request.POST.get('anonymous') == 'on'

        # Save complaint; if anonymous, student field is None
        Complaint.objects.create(
            student=None if anonymous else student,
            title=complaint_title,
            category=complaint_category,
            description=complaint_detail,
            status='Pending'
        )
        return redirect('dashboard:student_complain')

    complaints = Complaint.objects.filter(student=student).order_by("-created_at")
    return render(request, 'dashboard/student_complain.html', {"student": student, "complaints": complaints})


# ------------------------------
# Student leave requests
# ------------------------------
@login_required(login_url='login')
def student_leave_view(request):
    student = request.user.student

    if request.method == "POST":
        leave_type = request.POST.get("leave_type")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        reason = request.POST.get("reason")

        LeaveRecord.objects.create(
            student=student,
            leave_type=leave_type,
            start_date=start_date,
            end_date=end_date,
            reason=reason,
            status="Pending"
        )
        return redirect('dashboard:student_leave')

    leave_applications = LeaveRecord.objects.filter(student=student).order_by("-created_at")
    return render(request, 'dashboard/student_leave.html', {"student": student, "leave_applications": leave_applications})


# ------------------------------
# Teacher: update complaint status
# ------------------------------
@login_required(login_url='login')
def update_complaint_status(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)

    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status in ["Pending", "In Progress", "Resolved"]:
            complaint.status = new_status
            complaint.save()

    return redirect('dashboard:teacher_home')

#------------------------------
# Teacher: leave applications view
#------------------------------
@login_required
def teacher_leave_view(request):
    teacher = request.user.teacher
    # Filter leave applications for students in the teacher's class
    leave_applications = LeaveRecord.objects.filter(
        student__student_class=teacher.class_assigned
    ).order_by('-created_at')
    
    return render(request, 'dashboard/teacher_leave.html', {
        'teacher': teacher,
        'leave_applications': leave_applications
    })


@login_required
def update_leave_status(request, leave_id):
    leave = get_object_or_404(LeaveRecord, id=leave_id)
    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status in ["Approved", "Rejected"]:
            leave.status = new_status
            leave.save()
    return redirect('dashboard:teacher_leave')
