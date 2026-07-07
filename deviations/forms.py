from django import forms
from .models import DeviationLog

class DeviationLogForm(forms.ModelForm):
    class Meta:
        model = DeviationLog
        fields = ['title', 'description', 'immediate_action_taken', 'status', 'discovered_at', 'related_sop']
        widgets= {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows':4}),
            'immediate_action_taken': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'discovered_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'related_sop': forms.Select(attrs={'class': 'form-control'}),
        }