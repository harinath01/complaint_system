from django import forms

from complaints.models import Complaint


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['student_id', 'description', 'severity_level']

    def save(self, commit=True, staff=None):
        instance = super().save(commit=False)
        if staff:
            instance.staff = staff
        if commit:
            instance.save()
        return instance