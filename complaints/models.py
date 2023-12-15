from django.db import models
from django.contrib.auth.models import User


class Complaint(models.Model):
    SEVERITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    student_id = models.CharField(max_length=16)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    severity_level = models.CharField(max_length=10, choices=SEVERITY_CHOICES, default='low')

    def __str__(self):
        return f"Complaint by Staff: {self.staff.username} for Student ID: {self.student_id}"