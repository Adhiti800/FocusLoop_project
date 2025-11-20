from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    #department = models.CharField(max_length=50)
    your_subject = models.CharField(max_length=50)
    class_assigned = models.CharField(max_length = 50)
    #class_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} - {self.your_subject}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    roll_number = models.CharField(max_length =20, primary_key=True)
    student_class = models.CharField(max_length=50)
    section = models.CharField(max_length =5)

def __str__(self):
    return f"{self.user.username} - {self.your_subject}"
