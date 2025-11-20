from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Teacher, Student
from django.contrib.auth import logout


def welcome(request):
    if request.user.is_authenticated:
        return redirect('dashboard:home')
    return render(request, 'welcome.html')
    
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html', {})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('base:login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {"form": form})

@login_required
def teacher_info(request):
    if request.method == "POST":
        print(request.POST) 
        teacher_name = request.POST.get("teacher_name")
        #department = request.POST.get("department")
        your_subject = request.POST.get("your_subject")
        class_assigned = request.POST.get("class_assigned")
        #class_code = request.POST.get("class_code")
        # saves the data in database.

        Teacher.objects.create(
            user = request.user,
            teacher_name = teacher_name,
            your_subject = your_subject,
            class_assigned = class_assigned,

        )
        return redirect("dashboard:home")
    return render(request, "teacher_info.html")

@login_required
def student_info(request):
    if request.method == "POST":
        print(request.POST)
        student_name = request.POST.get("student_name")
        roll_number = request.POST.get("roll_number")
        student_class = request.POST.get("student_class")
        section = request.POST.get("section")

        Student.objects.create(
            user = request.user,
            student_name = student_name,
            roll_number = roll_number,
            student_class = student_class,
            section = section,
        )
        return redirect("dashboard: home")
    return render(request, "student_info.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard:home")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})
        
    return render(request, "base: login.html")


#def logout_view(request):
    #logout(request)
    #return redirect('welcome.html')

