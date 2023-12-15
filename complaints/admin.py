from django.contrib import admin
from .models import Complaint


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'description', 'staff', 'severity_level', 'timestamp')
    list_filter = ('severity_level', 'timestamp')
    search_fields = ('student_id', 'staff__username', 'description')
