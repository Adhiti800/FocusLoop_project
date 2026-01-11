from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Teacher, Students
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

# ===========================
# Welcome Pages
# ===========================
def welcome(request):
    if request.user.is_authenticated:
        return redirect('dashboard:home')  # unified dashboard router
    return render(request, 'welcome.html')


# ===========================
# Student Signup
# ===========================
def student_signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create student profile
          
            login(request, user)
            return redirect('base:student_info')  # student fills additional info
        else:
            print(form.errors)
            messages.error(request, "Signup failed. Please fix the errores.")
    else:
        form = UserCreationForm()
    return render(request, 'registration/student_signup.html', {"form": form})


# ===========================
# Teacher Signup
# ===========================
def teacher_signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create teacher profile

            login(request, user)
            return redirect('base:teacher_info')  # student fills additional info
        else:
            print(form.errors)
            messages.error(request, "Signup failed. Please fix the errores.")
           
    else:
        form = UserCreationForm()
    return render(request, 'registration/teacher_signup.html', {"form": form})


# ===========================
# Student Info
# ===========================

def student_info(request):
    if request.method == "POST":
        Students.objects.create(
            user=request.user,
            student_name=request.POST.get("student_name"),
            roll_number=request.POST.get("roll_number"),
            student_class=request.POST.get("student_class"),
            section=request.POST.get("section"),
        )
        return redirect("base:login")
    
    return render(request, "student_info.html")


# ===========================
# Teacher Info
# ===========================

def teacher_info(request):
    if request.method == "POST":
        Teacher.objects.create(
            user=request.user,
            teacher_name=request.POST.get("teacher_name"),
            your_subject=request.POST.get("your_subject"),
            class_assigned=request.POST.get("class_assigned"),
        )
        return redirect("base:login")  # sends teacher to their dashboard
    return render(request, "teacher_info.html")


# ===========================
# Login View
# ===========================
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.role == 'student':
                return redirect("dashboard:student_home")
            elif user.role == 'teacher':
                return redirect("dashboard:teacher_home")
            else:
                messages.error(request, "Invalid user role.")   
                return redirect("base:login")
        messages.error(request, "Invalid username or password.")
    return render(request, "login.html")  # fixed template path


# ===========================
# Logout View
# ===========================
def logout_view(request):
    logout(request)
    return redirect('base:welcome')

#==========================

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
