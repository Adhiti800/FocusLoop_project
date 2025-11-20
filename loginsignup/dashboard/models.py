from django.db import models
from datetime import date

class Student(models.Model):
    # ... student fields
    name = models.CharField(max_length=100)
    # ...

class LeaveRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()
    reason = models.TextField()
    is_approved = models.BooleanField(default=False)
    sent_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} Leave from {self.start_date}"