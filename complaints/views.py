from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ComplaintForm

def is_staff_user(user):
    return user.is_staff


@user_passes_test(is_staff_user)
def create_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save(staff=request.user)
            messages.success(request, 'Complaint submitted successfully!')
            return redirect('create_complaint')
    else:
        form = ComplaintForm()

    return render(request, 'create_complaint.html', {'form': form})

