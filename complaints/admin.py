from django.contrib import admin
from .models import Complaint


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'department', 'staff', 'complaint_type', 'timestamp')
    list_filter = ("complaint_type", "department", 'timestamp')
    search_fields = ('student_id', 'staff__username')
