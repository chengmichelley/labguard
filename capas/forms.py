from django import forms
from .models import CapaAction

class CapaActionForm(forms.ModelForm):
    class Meta:
        model = CapaAction
        fields = ['title', 'root_cause', 'preventive_action', 'status', 'due_date', 'related_deviation']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'root_cause': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
            'preventive_action': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'related_deviation': forms.Select(attrs={'class': 'form-control'}),
        }