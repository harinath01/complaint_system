from django.db import models
from django.contrib.auth.models import User


class Complaint(models.Model):
    DEPARTMENT_CHOICES = [
        ('B.E', [
            ('B.E_AGRI', 'B.E - Agricultural Engineering'),
            ('B.E_AI&DS', 'B.E - Artificial Intelligence and Data Science'),
            ('B.E_BME', 'B.E - Biomedical Engineering'),
            ('B.E_BT', 'B.E - Biotechnology'),
            ('B.E_CSE', 'B.E - Computer Science and Engineering'),
            ('B.E_CSE_B', 'B.E - Computer Science and Engineering - B'),
            ('B.E_ECE', 'B.E - Electronics and Communication Engineering'),
            ('B.E_IT', 'B.E - Information Technology'),
            ('B.E_MECH', 'B.E - Mechanical Engineering'),
        ]),
        ('S&H', [
            ('S&H_AGRI', 'S&H - Agriculture'),
            ('S&H_AIML', 'S&H - Artificial Intelligence and Machine Learning'),
            ('S&H_AI&DS', 'S&H - Artificial Intelligence and Data Science'),
            ('S&H_BME', 'S&H - Biomedical Engineering'),
            ('S&H_BT', 'S&H - Biotechnology'),
            ('S&H_CSE', 'S&H - Computer Science and Engineering'),
            ('S&H_CSE_B', 'S&H - Computer Science and Engineering - B'),
            ('S&H_ECE', 'S&H - Electronics and Communication Engineering'),
            ('S&H_MECH', 'S&H - Mechanical Engineering'),
            ('S&H_IT', 'S&H - Information Technology'),
        ]),
        ('BSC', [
            ('BSC_IT', 'BSC - IT'),
            ('BSC_CY', 'BSC - Cybersecurity'),
            ('BSC_AI&DS', 'BSC - Artificial Intelligence and Data Science'),
            ('BSC_CS', 'BSC - Computer Science'),
        ]),
    ]

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
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)

    def __str__(self):
        return f"Complaint by Staff: {self.staff.username} for Student ID: {self.student_id}"