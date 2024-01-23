from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ComplaintForm
from .models import Complaint


def is_staff_user(user):
    return user.is_staff


@user_passes_test(is_staff_user)
def create_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data["student_id"]
            if has_duplicate_complaint(request.user, student_id):
                messages.error(request,
                               'You have already submitted a complaint for this student today.')
            else:
                form.save(staff=request.user)
                complaints_count = Complaint.objects.filter(staff=request.user, student_id=student_id).count()
                if complaints_count >= 2:
                    messages.error(request, f'Complaint submitted successfully! Student reached {complaints_count} complaints')
                else:
                    messages.success(request, 'Complaint submitted successfully!')
            return redirect('create_complaint')
    else:
        form = ComplaintForm()

    return render(request, 'create_complaint.html', {'form': form})


def has_duplicate_complaint(user, student_id):
    today = timezone.now().date()
    return Complaint.objects.filter(staff=user, student_id=student_id, timestamp__date=today).exists()
