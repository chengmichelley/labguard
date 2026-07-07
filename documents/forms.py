from django import forms
from .models import ControlledDocument

class ControlledDocumentForm(forms.ModelForm):
    class Meta:
        model = ControlledDocument
        fields = ['title', 'filename', 'category', 'document_url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Equipment Manual'}),
            'filename': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., manual_v2.pdf'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'e.g., Regulatory Standard'}),
            'document_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
        }
        