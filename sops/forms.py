from django import forms 
from .models import SopDocument

class SopDocumentForm(forms.ModelForm):
    class Meta:
        model = SopDocument
        fields = [
            'title', 'doc_number', 'version', 'status', 'author_department', 'purpose_scope', 'roles_responsibilities', 'tools_equipment', 'procedure_steps', 'safety_compliance', 'approved_by', 'effective_date'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'doc_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., SOP-LAB-001'}),
            'version': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'author_department': forms.TextInput(attrs={'class': 'form-control'}),
            'approved_by': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'QA / Lab Manager Sign-off' }),
            'effective_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            
            'purpose_scope': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
            'roles_responsiblities': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tools_equipment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'procedure_steps': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'safety_compliance': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }