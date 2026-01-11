from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Profile(models.Model):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=100, default = "")
    your_subject = models.CharField(max_length=50, default = "")
    class_assigned = models.CharField(max_length=50, default = "")

    def __str__(self):
        return f"{self.teacher_name} - {self.your_subject}"
     
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student') 
    student_name = models.CharField(max_length=100, default = "")
    roll_number = models.CharField(max_length=20, unique = True)
    student_class = models.CharField(max_length=50, default = "")
    section = models.CharField(max_length=5, default = "")

    def __str__(self):
        return f"{self.student_name} - {self.student_class} {self.section}"
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

