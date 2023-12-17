from django.db import models
from django.contrib.auth.models import User


class Complaint(models.Model):
    COMPLAINT_TYPES = [
        ('dresscode', 'Improper dress code'),
        ('informal_shoe', 'Informal shoe'),
        ('hairstyle', 'Improper hairstyle'),
        ('untrimmed_beard', 'Untrimmed beard'),
        ('socks_not_worn', 'Socks not worn'),
        ('shoes_not_worn', 'Shoes not worn'),
        ('blazer_not_worn', 'Blazer not worn'),
    ]

    student_id = models.CharField(max_length=16)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    complaint_type = models.CharField(max_length=20, choices=COMPLAINT_TYPES)

    def __str__(self):
        return f"Complaint by Staff: {self.staff.username} for Student ID: {self.student_id}"