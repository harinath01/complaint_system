from django import forms
from .models import Complaint


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['student_id', 'complaint_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['complaint_type'].widget = forms.Select(choices=Complaint.COMPLAINT_TYPES)

    def save(self, commit=True, staff=None):
        instance = super().save(commit=False)
        if staff:
            instance.staff = staff
        if commit:
            instance.save()
        return instance
