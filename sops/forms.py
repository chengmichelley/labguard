from django import forms 
from .models import SopDocument

class SopDocumentForm(forms.ModelForm):
    class Meta:
        model = SopDocument
        fields = ['title', 'doc_number', 'version', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'doc_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., SOP-LAB-001'}),
            'version': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }