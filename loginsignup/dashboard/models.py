from django.db import models
from datetime import date
from django.contrib.auth.models import User
from base.models import Students, Teacher
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

class Students(models.Model):
    # ... student fields
    name = models.CharField(max_length=100, default = "")
    # ...

class LeaveRecord(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length = 100)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length = 20, default = "Pending")
    created_at =models.DateTimeField(auto_now_add = True)
    is_approved = models.BooleanField(default=False)
    sent_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} Leave from {self.start_date}"
    
class Student_complaints(models.Model):
    student = models.ForeignKey(Students, on_delete = models.SET_NULL, null = True, blank = True)
    complaint_title = models.CharField(max_length=200)
    complaint_category = models.CharField(max_length=50)
    complaint_description = models.TextField()
    status = models.CharField(max_length = 20, default = "Pending")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Complaint(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, default="Pending")  # Pending, In Progress, Resolved
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.status}"
    
@login_required
def teacher_dashboard(request):
    teacher = request.user.teacher
    complaints = Complaint.objects.all().order_by('-created_at')
    return render(request, "dashboard/teacher_home.html", {"teacher": teacher, "complaints": complaints})


@login_required
def update_complaint_status(request, id):
    if request.method == "POST":
        complaint = Complaint.objects.get(id=id)
        complaint.status = request.POST.get("status")
        complaint.save()
    return redirect('dashboard:teacher_home')





    




    