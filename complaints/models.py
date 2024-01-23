from django.db import models
from django.contrib.auth.models import User


class Complaint(models.Model):
    DEPARTMENT_CHOICES = [
        ('B.E.', [
            ('B.E_BME', 'B.E - Bio medical Engineering'),
            ('B.E_CSE', 'B.E - Computer Science and Engineering'),
            ('B.E_CSE_B', 'B.E - Computer Science and Engineering (RL)'),
            ('B.E_ECE', 'B.E - Electronics and Communication Engineering'),
            ('B.E_MECH', 'B.E - Mechanical Engineering'),
        ]),
        ('B.Tech', [
            ('BTECH_AE', 'B.Tech - Agricultural Engineering'),
            ('BTECH_AI&DS', 'B.Tech - Artificial Intelligence and Data Science'),
            ('BTECH_BT', 'B.Tech - Bio-Technology'),
            ('BTECH_IT', 'B.Tech - Information Technology'),
        ]),
        ('B.Sc.', [
            ('BSC_IT', 'B.Sc. Information Technology'),
            ('BSC_CY', 'B.Sc. Cybersecurity'),
            ('BSC_AI&DS', 'B.Sc. Artificial Intelligence and Data Science'),
            ('BSC_CS', 'B.Sc. Computer Science'),
        ]),
        ('S&H', [
            ('S&H_AGRI', 'S&H - Agricultural'),
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