from django import forms
from .models import TrainingRecord

class TrainingRecordForm(forms.ModelForm):
    class Meta:
        model = TrainingRecord
        fields = ['employee_name', 'related_sop', 'status', 'due_date']
        widgets = {
            'employee_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Jane Doe'}),
            'related_sop': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }