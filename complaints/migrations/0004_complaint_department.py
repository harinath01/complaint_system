# Generated by Django 4.2.8 on 2024-01-16 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("complaints", "0003_alter_complaint_complaint_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="complaint",
            name="department",
            field=models.CharField(
                choices= [
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
                ],
                default=1,
                max_length=20,
            ),
            preserve_default=False,
        ),
    ]